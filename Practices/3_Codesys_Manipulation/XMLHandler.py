import xml.etree.ElementTree as ET

# from argsHandler import (ProjectFile, RemoveDevice, RemoveConnector, AddDevice, AddConnector,
#                          DeviceDescription, AddLibrary, AddPlaceholder, RemoveLibrary, RemovePlaceholder,
#                          Library, Instance, Target, Arguments)
import os

class XMLHandler:
    def __init__(self, projectFile, deviceDescription, library):
        self.path = os.path.join(projectFile.path, projectFile.backupXMLName)
        self.projectFile = projectFile
        self.library= library
        self.deviceDescription = deviceDescription
        self.tree = None
        self.root = None

        self.initialise()

    def initialise(self):
        # Load the XML file
        self.tree = ET.parse(self.path)
        self.root = self.tree.getroot()
        self.strip_namespaces(self.root)

    def strip_namespaces(self, root):
        """Recursively remove all namespaces from XML element tags."""
        for el in root.iter():
            if '}' in el.tag:
                el.tag = el.tag.split('}', 1)[1]
            # Also strip attribute namespaces if needed
            el.attrib = {k.split('}', 1)[-1] if '}' in k else k: v for k, v in el.attrib.items()}

    def process(self):
        # Check add device
        if self.deviceDescription.addDevice is not None:
            print("An add device is detected..")
            self.add_device(self.deviceDescription.addDevice)

        # Check add connector
        if self.deviceDescription.addConnector is not None:
            print("An add connector is detected..")
            self.add_connector(self.deviceDescription.addConnector)

        # Check remove device
        if self.deviceDescription.removeDevice is not None:
            print("A remove device is detected..")
            self.remove_device(self.deviceDescription.removeDevice)

        # Check remove connector
        if self.deviceDescription.removeConnector is not None:
            print("A remove connector is detected..")
            self.remove_connector(self.deviceDescription.removeConnector)

        # Check add libraries
        if self.library.addLibraries is not None:
            print("An add library is detected..")
            for addLibrary in self.library.addLibraries:
                print("Adding library {}..".format(addLibrary.name))
                self.add_library(addLibrary)

        # Check add placeholders
        if self.library.addPlaceholders is not None:
            print("An add placeholder is detected..")
            for addPlaceholder in self.library.addPlaceholders:
                print("Adding placeholder {}..".format(addPlaceholder.placeholder))
                self.add_placeholder(addPlaceholder)

        # Check remove libraries
        if self.library.removeLibraries is not None:
            print("A remove library is detected..")
            for removeLibrary in self.library.removeLibraries:
                print("Removing library {}..".format(removeLibrary.namespace))
                self.remove_library(removeLibrary)

        # Check remove placeholders
        if self.library.removePlaceholders is not None:
            print("A remove placeholder is detected..")
            for removePlaceholder in self.library.removePlaceholders:
                print("Removing placeholder {}..".format(removePlaceholder.placeholder))
                self.remove_placeholder(removePlaceholder)

    def add_device(self, addDevice):
        print("Searching the parent element to add a device")
        device_type = self.root.find(".//DeviceType")
        if device_type is not None:
            identification = ET.SubElement(device_type, "DeviceIdentification")

            type = ET.SubElement(identification, "Type")
            type.text = addDevice.type

            id = ET.SubElement(identification, "Id")
            id.text = addDevice.id

            version = ET.SubElement(identification, "Version")
            version.text = addDevice.version

            print("Added a device successfully : {}".format(addDevice.id))

    def add_connector(self, addConnector):
        print("Searching the parent element to add a connector")
        device_type = self.root.find(".//DeviceType")
        if device_type is not None:
            print("Found the device type element")

            ET.SubElement(device_type, "Connector", {
                "moduleType" : addConnector.moduleType,
                "interface" : addConnector.interface,
                "connectorId" : addConnector.connectorId
            })
            print("Added a connector successfully : {}".format(addConnector.interface))
        else:
            print("Could not find the device type element")

    def remove_device(self, removeDevice):
        print("Searching the parent element to remove a device")
        device_type = self.root.find(".//DeviceType")
        if device_type is not None:
            print("Found the device type element")
            identifications = device_type.findall(".//DeviceIdentification")
            for identification in identifications:
                id = identification.find(".//Id")
                if id is not None and id.text == removeDevice.id:
                    device_type.remove(identification)
                    print("Removed a device successfully : {}".format(removeDevice.id))
        else:
            print("Could not find the device type element")

    def remove_connector(self, removeConnector):
        print("Searching the parent element to remove a connector")
        device_type = self.root.find(".//DeviceType")
        if device_type is not None:
            print("Found the device type element")
            connectors = device_type.findall(".//Connector")
            for connector in connectors:
                if connector.attrib["interface"] == removeConnector.interface:
                    device_type.remove(connector)
                    print("Removed a connector successfully : {}".format(removeConnector.interface))
        else:
            print("Could not find the device type element")

    def add_library(self, addLibrary):
        print("Searching the parent element to add a library")
        libraries = self.root.find(".//Libraries")
        if libraries is not None:
            library = ET.SubElement(libraries, "Library", {
                "Name": addLibrary.name,
                "Namespace": addLibrary.namespace,
                "HideWhenReferencedAsDependency": addLibrary.hideWhenReferencedAsDependency,
                "PublishSymbolsInContainer": addLibrary.publishSymbolsInContainer,
                "SystemLibrary": addLibrary.systemLibrary,
                "LinkAllContent": addLibrary.linkAllContent,
                "DefaultResolution": addLibrary.defaultResolution
            })
            print("Added a library successfully : {}".format(addLibrary.name))
        else:
            print("Could not find the Libraries element")

    def add_placeholder(self, addPlaceholder):
        print("Searching the parent element to add a placeholder")
        libraries = self.root.find(".//Libraries")
        if libraries is not None:
            redirections = libraries.find(".//PlaceholderRedirections")
            if redirections is not None:
                placeholder = ET.SubElement(redirections, "PlaceholderRedirection", {
                    "Placeholder" : addPlaceholder.placeholder,
                    "Redirection" : addPlaceholder.redirection
                })
                print("Added a placeholder successfully : {}".format(addPlaceholder.placeholder))
            else:
                print("Could not find the PlaceholderRedirections element")
        else:
            print("Could not find the Libraries element")

    def remove_library(self, removeLibrary):
        print("Searching the parent element to remove a library")
        libraries_element = self.root.find(".//Libraries")
        if libraries_element is not None:
            libraries = libraries_element.findall(".//Library")
            for library in libraries:
                if library.attrib["Namespace"] == removeLibrary.namespace:
                    libraries_element.remove(library)
                    print("Removed a library successfully : {}".format(removeLibrary.namespace))
        else:
            print("Could not find the Libraries element")

    def remove_placeholder(self, removePlaceholder):
        print("Searching the parent element to remove a placeholder")
        libraries = self.root.find(".//Libraries")
        if libraries is not None:
            redirections = libraries.find(".//PlaceholderRedirections")
            if redirections is not None:
                placeholders = redirections.findall(".//PlaceholderRedirection")
                for placeholder in placeholders:
                    if placeholder.attrib["Placeholder"] == removePlaceholder.placeholder:
                        redirections.remove(placeholder)
                        print("Removed a placeholder successfully : {}".format(removePlaceholder.placeholder))
            else:
                print("Could not find the PlaceholderRedirections element")
        else:
            print("Could not find the Libraries element")

    def save_xml_file(self):
        path = os.path.join(self.projectFile.path, self.projectFile.editedXMLName)
        self.tree.write(path, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    import Util
    test_argument_path = "test_arguments.json"
    sample_xml_path = "test_project.xml"
    output_xml_path = "test_project_output.xml"

    test_argument = Util.get_arguments_instance(test_argument_path)

    # create a xml handler with test arguments
    handler = XMLHandler(projectFile=test_argument.projectFile, library=test_argument.library, deviceDescription=test_argument.deviceDescription)

    # manipulate the xml file according to the arguments
    handler.process()

    # save the manipulated xml
    handler.save_xml_file()


