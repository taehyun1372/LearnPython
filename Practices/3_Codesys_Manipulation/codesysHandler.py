import json
import sys, os
import time
from XMLHandler import XMLHandler
from System.Net import IPAddress

class ExReporter(ExportReporter):
    def error(self, message):
        print(message)
    def warning(self, message):
        print(message)
    def nonexportable(self, message):
        print(message)
    @property
    def aborting(self):
        return False

# Create the import reporter
class ImReporter(ImportReporter):
    def error(self, message):
        system.write_message(Severity.Error, message)

    def warning(self, message):
        system.write_message(Severity.Warning, message)

    def resolve_conflict(self, obj):
        return ConflictResolve.Copy

    def added(self, obj):
        print("added: ", obj)

    def replaced(self, obj):
        print("replaced: ", obj)

    def skipped(self, obj):
        print("skipped: ", obj)

    @property
    def aborting(self):
        return False

class CodesysHandler:
    def __init__(self):
        pass

    def export_xml(self, projectFile, target):
        try:
            project = projects.primary
            print("Searching for the target device - {}".format(target.deviceName))
            device = project.find(target.deviceName, True)
            if device is not None:
                # Get a reporter instance
                print("Found the target device - {}".format(device[0].get_name()))
                reporter = ExReporter()
                backup_path = os.path.join(projectFile.path, projectFile.backupXMLName)
                print("Making a backup file at {}".format(backup_path))
                project.export_xml(reporter=reporter, objects=device, path=backup_path, recursive=True, export_folder_structure=True)
            else:
                print("The specified device has not been found..{}".format(target.deviceName))
                sys.exit(1)

        except Exception as e:
            print("Failed to export xml file..{}".format(e))

    def import_xml(self, projectFile):
        try:
            project = projects.primary
            project.close()

            # Create the reporter instance
            reporter = ImReporter()

            target_project = os.path.join(projectFile.path, projectFile.name)
            print("Creating a new project at - {}".format(target_project))
            # Create the new project
            new_project = projects.create(target_project, True)

            edited_path = os.path.join(projectFile.path, projectFile.editedXMLName)
            print("Importing xml file at - {}".format(edited_path))
            # Import the data into the project
            new_project.import_xml(reporter, edited_path)

            # Save the project to the specified path
            new_project.save()

        except Exception as e:
            print("Failed to import xml file..{}".format(e))

    def build(self, target):
        try:
            proj = projects.primary
            # Find the first Application object in the project
            application = proj.find(target.applicationName, recursive=True)[0]
            if not application:
                print("No Application found..{}".format(target.applicationName))
            else:
                application.clean()
                application.rebuild()
                print("Built the application successfully")
        except Exception as e:
            print("Failed to build application..{}".format(e))

    def online(self, target):
        try:
            proj = projects.primary
            # Finds the object in the project, and return the first result
            device = proj.find(target.deviceName, True)[0]
            if device is None:
                print("Failed to find the target device")
            else:
                print("Found the target device - {}".format(device.get_name()))
                matching_gateway = False
                gateway_names = []
                target_gateway_name = target.gatewayName

                gateways = online.gateways

                for gateway in gateways:
                    gateway_names.append(gateway.name)
                    if (gateway.config_params[0] == target.gatewayIPAddress and  # Check ip address
                            gateway.config_params[1] == target.gatewayPort):  # Check port
                        matching_gateway = True # Found the existing gateway
                        target_gateway_name = gateway.name
                        print('Found the target gateway..{}'.format(target_gateway_name))
                        break

                if not matching_gateway:
                    print('No matching gateway found..creating a new gateway..{}'.format(target_gateway_name))

                    params = {
                        0: target.gatewayIPAddress,  # or use param.id == 0
                        1: target.gatewayPort  # or use param.id == 1
                    }

                    while target_gateway_name in gateway_names: #if there is duplicated gateway, use a different gateway name
                        prefix, suffix = target_gateway_name.split('-')
                        target_gateway_name = prefix + '-' + str(int(suffix) + 1)

                    gateways.add_new_gateway(target_gateway_name, params)

                for instance in target.instances:
                    ip = IPAddress.Parse(instance.ipAddress)
                    print("Connecting to target instance {}, {}".format(instance.id, instance.ipAddress))
                    device.set_gateway_and_ip_address(target_gateway_name, ip)

                    online_application = online.create_online_application()
                    online_device = online_application.get_online_device()

                    online.set_specific_credentials(target=online_device, username=instance.id,
                                                    password=instance.password)
                    online_device.connect()
                    online_application.login(OnlineChangeOption.Try, True)

                    user_name = online_device.current_logged_on_username
                    print("Connected to target instance {}".format(user_name))

                    time.sleep(3)  # This is small delay before starting the application

                    state = online_application.application_state
                    if state == ApplicationState.run:
                        print("Application already running..")
                    elif state == ApplicationState.stop:
                        print("Application stopped.")
                        online_application.start()
                        print("Application now started.")
                    else:
                        print("Application state: {}".format(state))

                    online_application.logout()
                    online_device.forced_disconnect()


        except Exception as e:
            print("Failed to download the application..{}".format(e))


class DictToObject:
    def __init__(self, d):
        for k, v in d.items():
            if isinstance(v, dict):
                v = DictToObject(v)
            elif isinstance(v, list):
                v = [DictToObject(i) if isinstance(i, dict) else i for i in v]
            setattr(self, k, v)

def from_dict(d):
    if isinstance(d, dict):
        return DictToObject(d)
    elif isinstance(d, list):
        return [from_dict(i) for i in d]
    else:
        return d

# Wrong argument
if len(sys.argv) < 2:
    sys.exit(1)

print("Hello World")
full_path = ' '.join(sys.argv[1:])

print(full_path)
with open(full_path, "r") as f:
    raw_data = json.load(f)
    arguments = from_dict(raw_data)

    print(arguments.target.deviceName)
    codesysHandler = CodesysHandler()
    codesysHandler.export_xml(projectFile=arguments.projectFile, target=arguments.target)

    xmlHandler = XMLHandler(projectFile=arguments.projectFile, deviceDescription=arguments.deviceDescription, library=arguments.library)
    xmlHandler.process()
    xmlHandler.save_xml_file()
    codesysHandler.import_xml(projectFile=arguments.projectFile)
    codesysHandler.build(target=arguments.target)
    codesysHandler.online(target=arguments.target)
