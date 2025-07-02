import json
import sys, os
import time
from XMLHandler import XMLHandler
from System.Net import IPAddress

def get_backup_xml_path(files):
    backup_xml_name = files.projectName.split('.')[0] + files.backupXMLName + ".xml"
    return os.path.join(files.projectPath, backup_xml_name)

def get_edited_xml_path(files):
    edited_xml_name = files.projectName.split('.')[0] + files.editedXMLName + ".xml"
    return os.path.join(files.projectPath, edited_xml_name)

def get_new_project_path(files):
    new_project_name = files.projectName.split('.')[0] + files.newProjectName + ".project"
    return os.path.join(files.projectPath, new_project_name)

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

    def export_xml(self, device_name, xml_path):
        try:
            project = projects.primary
            print("Searching for the target device - {}".format(device_name))
            device = project.find(device_name, True)
            if device is None:
                print("The specified device has not been found..{}".format(device_name))
                sys.exit(1)
            else:
                # Get a reporter instance
                print("Found the target device - {}".format(device[0].get_name()))
                reporter = ExReporter()
                # Export xml file
                print("Making a backup file at {}".format(xml_path))
                project.export_xml(reporter=reporter, objects=device, path=xml_path, recursive=True, export_folder_structure=True)
                print("The target device successfully exported")

        except Exception as e:
            print("Failed to export xml file..{}".format(e))
            sys.exit(1)

    def import_xml(self, new_project_path, xml_path):
        try:
            # close the current project
            project = projects.primary
            project.close()

            # Create the reporter instance
            reporter = ImReporter()

            print("Creating a new project at - {}".format(new_project_path))
            # Create the new project
            new_project = projects.create(new_project_path, True)

            # Import the edited xml into the project
            print("Importing xml file at - {}".format(xml_path))
            new_project.import_xml(reporter, xml_path)

            # Save the project to the specified path
            new_project.save()

        except Exception as e:
            print("Failed to import xml file..{}".format(e))
            sys.exit(1)

    def build(self, application_name):
        try:
            proj = projects.primary
            # Find the first Application object in the project
            application = proj.find(application_name, recursive=True)[0]
            if not application:
                print("No Application found..{}".format(application_name))
                sys.exit(1)
            else:
                application.clean()
                application.rebuild()
                print("Built the application successfully")
        except Exception as e:
            print("Failed to build application..{}".format(e))
            sys.exit(1)

    def set_gateway(self, device_name, gateway_name, gateway_ip_address, gateway_port):
        try:
            proj = projects.primary
            # Finds the object in the project, and return the first result
            device = proj.find(device_name, True)[0]
            if device is None:
                print("Failed to find the target device".format(device_name))
                sys.exit(1)
            else:
                print("Found the target device - {}".format(device.get_name()))
                matching_gateway = False
                gateway_names = []
                target_gateway_name = gateway_name

                gateways = online.gateways

                for gateway in gateways:
                    gateway_names.append(gateway.name)
                    if (gateway.config_params[0] == gateway_ip_address and  # Check ip address
                            gateway.config_params[1] == gateway_port):  # Check port
                        matching_gateway = True # Found the existing gateway
                        target_gateway_name = gateway.name
                        print('Found the target gateway..{}'.format(target_gateway_name))
                        break

                if not matching_gateway:
                    params = {
                        0: gateway_ip_address,  # or use param.id == 0
                        1: gateway_port  # or use param.id == 1
                    }

                    while target_gateway_name in gateway_names: #if there is duplicated gateway, use a different gateway name
                        prefix, suffix = target_gateway_name.split('-')
                        target_gateway_name = prefix + '-' + str(int(suffix) + 1)

                    print('No matching gateway found..creating a new gateway..{}'.format(target_gateway_name))
                    gateways.add_new_gateway(target_gateway_name, params)

                return target_gateway_name
        except Exception as e:
            print("Failed to set the gateway..{}".format(e))
            sys.exit(1)

    def online(self, device_name, gateway_name, instance_ip_address, instance_id, instance_password):
        try:
            proj = projects.primary
            # Finds the object in the project, and return the first result
            device = proj.find(device_name, True)[0]
            if device is None:
                print("Failed to find the target device".format(device_name))
                sys.exit(1)
            else:
                ip = IPAddress.Parse(instance_ip_address)

                print("Connecting to target instance {} - {}".format(instance_id, instance_ip_address))
                device.set_gateway_and_ip_address(gateway_name, ip)

                online_application = online.create_online_application()
                online_device = online_application.get_online_device()

                online.set_specific_credentials(target=online_device, username=instance_id,
                                                password=instance_password)
                online_device.connect()
                online_application.login(OnlineChangeOption.Try, True)

                instance_id = online_device.current_logged_on_username
                print("Successfully logged in to target instance {}".format(instance_id))

                time.sleep(2)  # This is small delay before starting the application

                # Start the application if it is not started
                state = online_application.application_state
                if state == ApplicationState.run:
                    print("Application is already running..")
                elif state == ApplicationState.stop:
                    print("Application is stopped..")
                    online_application.start()
                    print("Application is now started..")
                else:
                    print("Application state: {}".format(state))

                # Log out from the application
                online_application.logout()
                online_device.forced_disconnect()

                return instance_id

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
    print("arguments have not been passed correctly")
    sys.exit(1)

temp_args_file_path = ' '.join(sys.argv[1:])

print(temp_args_file_path)
with open(temp_args_file_path, "r") as f:
    raw_data = json.load(f)
    arguments = from_dict(raw_data)

    print(arguments.target.deviceName)
    codesysHandler = CodesysHandler()
    backup_xml_path = get_backup_xml_path(files=arguments.files)
    codesysHandler.export_xml(device_name=arguments.target.deviceName, xml_path=backup_xml_path)

    xmlHandler = XMLHandler(xml_path=backup_xml_path, deviceDescription=arguments.deviceDescription, library=arguments.library)
    xmlHandler.process()
    edited_xml_path = get_edited_xml_path(files=arguments.files)
    xmlHandler.save_xml_file(edited_xml_path)

    new_project_path = get_new_project_path(files=arguments.files)
    codesysHandler.import_xml(new_project_path=new_project_path, xml_path=edited_xml_path)
    codesysHandler.build(application_name=arguments.target.applicationName)
    gateway_name = codesysHandler.set_gateway(device_name=arguments.target.deviceName, gateway_name=arguments.target.gatewayName, gateway_ip_address=arguments.target.gatewayIPAddress, gateway_port=arguments.target.gatewayPort)

    if gateway_name is None:
        print("gateway setting has not been done correctly..{}".format(gateway_name))
        sys.exit(1)

    setup_instances = []
    for instance in arguments.target.instances:
        setup_instance = codesysHandler.online(device_name=arguments.target.deviceName, gateway_name=gateway_name, instance_ip_address=instance.ipAddress, instance_id=instance.id, instance_password=instance.password)
        if setup_instance is not None:
            setup_instances.append(setup_instance)

    print("Successfully setup {} instances - {}".format(len(setup_instances), setup_instances))