# from argsHandler import (ProjectFile, RemoveDevice, RemoveConnector, AddDevice, AddConnector,
#                          DeviceDescription, AddLibrary, AddPlaceholder, RemoveLibrary, RemovePlaceholder,
#                          Library, Instance, Target, Arguments)
import sys

# Create the export reporter
class Reporter(ExportReporter):
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
class Reporter(ImportReporter):
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

    def export_xml(self, deviceName, backupXMLName):
        try:
            project = projects.primary
            device = project.find(deviceName, True)[0]
            if device is not None:
                # Get a reporter instance
                reporter = Reporter()

                project.export_xml(reporter=reporter, objects=device, path=backupXMLName, recursive=True, export_folder_structure=True)
            else:
                print("The specified device has not been found..{}".format(deviceName))
                sys.exit(1)

        except Exception as e:
            print("Failed to export xml file")


if __name__ == "__main__":
    import json
    test_argument_path = "test_arguments.json"
    try:
        with open(test_argument_path, 'r') as f:
            data = json.load(f)

            deviceName = data["target"]["deviceName"]
            backupXMLName = data["projectFile"][""]
            
            codesysHandler = CodesysHandler()
            codesysHandler.export_xml(deviceName=deviceName, backupXMLName=backupXMLName)

    except Exception as e:
        print("Invalid JSON: {}".format{e})