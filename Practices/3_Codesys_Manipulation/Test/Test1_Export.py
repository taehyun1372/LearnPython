import os

# Specify the object which should be exported
DEVICE_NAME = "Codesys_Control_Win_V3"

# Define the path where the exported objects should be stored
TARGET_PATH = r"C:\Users\a00533064\OneDrive - ONEVIRTUALOFFICE\Desktop\Code\LearnPython\Practices\3_Codesys_Manipulation\Test\Modbus_Test_Project.xml"

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

proj = projects.primary

if proj is None:
    print("No project is currently opened!")
else:
        # Finds the object in the project, and return the first result
        device = proj.find(DEVICE_NAME, True)
        if device is not None:
            print(device[0].get_name())

        # Get a reporter instance
        reporter = Reporter()

        proj.export_xml(reporter=reporter, objects=device, path=TARGET_PATH, recursive=True, export_folder_structure=True)

        print("Successfully Exported")

