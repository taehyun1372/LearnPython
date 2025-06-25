import os

# Specify the object which should be exported
object_name = "CODESYS_Control_Win_V3"

# Define the path where the exported objects should be stored
object_path = r"C:\Temp"


# Define the printing function
def print_tree(treeobj, depth=0):
    name = treeobj.get_name(False)
    if treeobj.is_device:
        deviceid = treeobj.get_device_identification()
        print("{0} - {1} {2}".format(" " * depth, name, deviceid))

    for child in treeobj.get_children(False):
        print_tree(child, depth + 1)


# Create the export reporter
class Reporter(ExportReporter):
    def error(self, message):
        system.write_message(Severity.Error, message)

    def warning(self, message):
        system.write_message(Severity.Warning, message)

    def nonexportable(self, message):
        print(message)

    @property
    def aborting(self):
        return False


try:
    # Get the project reference of the currently opened project
    project_reference = projects.primary

    # Get a reporter instance
    reporter = Reporter()

    # Print all devices in the project
    for obj in project_reference.get_children():
        print_tree(obj)

    # Finds the object in the project, and return the first result
    device = project_reference.find(object_name, True)

    if device != None:
        filename = os.path.join(object_path, device[0].get_name() + ".xml")
        print(device[0].get_name())
        # Exports the object to the hard drive
        project_reference.export_xml(reporter, device, filename, True, True)

except Exception as exception:
    print("Error: " + str(exception))
    if not system.trace:
        print("Please turn on the 'Script Tracing' function to get detailed information about the script execution.")