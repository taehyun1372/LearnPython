import os

# Specify the project file name
PROJECT_PATH = r"C:\Users\a00533064\OneDrive - ONEVIRTUALOFFICE\Desktop\Code\LearnPython\Practices\3_Codesys_Manipulation\Modbus_Test_Project_Imported.project"

# Define the path where the project should be/is storedproject_path = r"C:\Python"

# Define the file where the exported object is stored
FILE_NAME = r"C:\Users\a00533064\OneDrive - ONEVIRTUALOFFICE\Desktop\Code\LearnPython\Practices\3_Codesys_Manipulation\Modbus_Test_Project_Edited.xml"


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


try:
    # Clean up any open project
    if projects.primary:
        projects.primary.close()

    # Create the reporter instance
    reporter = Reporter()

    # Create the new project
    project_reference = projects.create(PROJECT_PATH, True)

    # Import the data into the project
    project_reference.import_xml(reporter, FILE_NAME)

    # Save the project to the specified path
    project_reference.save()
except Exception as exception:
    print("Error: " + str(exception))
    if not system.trace:
        print("Please turn on the 'Script Tracing' function to get detailed information about the script execution.")