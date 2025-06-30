import json
import sys, os

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
