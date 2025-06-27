import xml.etree.ElementTree as ET
from symbol import argument

from argsHandler import (ProjectFile, RemoveDevice, RemoveConnector, AddDevice, AddConnector,
                         DeviceDescription, AddLibrary, AddPlaceholder, RemoveLibrary, RemovePlaceholder,
                         Library, Instance, Target, Arguments)
import os

class XMLHandler:
    def __init__(self, path, deviceDescription: DeviceDescription, library: Library):
        self.path = path
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
        # Check remove device
        if self.deviceDescription.removeDevice is not None:
            print("A remove device is detected..")
            self.remove_device(self.deviceDescription.removeDevice)

        # Check add device
        if self.deviceDescription.addDevice is not None:
            print("An add device is detected..")
            self.add_device(self.deviceDescription.addDevice)

        # Check remove connector
        if self.deviceDescription.removeConnector is not None:
            print("A remove connector is detected..")
            self.remove_connector(self.deviceDescription.removeConnector)

        # Check add connector
        if self.deviceDescription.addConnector is not None:
            print("An add connector is detected..")
            self.add_connector(self.deviceDescription.addConnector)

        # Check remove libraries
        if self.library.removeLibraries is not None:
            print("A remove library is detected..")
            for name, removeLibrary in self.library.removeLibraries.items():
                print(f"Removing library {name}..")
                self.remove_library(removeLibrary)

        # Check add libraries
        if self.library.addLibraries is not None:
            print("An add library is detected..")
            for name, addLibrary in self.library.addLibraries.items():
                print(f"Adding library {name}..")
                self.add_library(addLibrary)

        # Check remove placeholders
        if self.library.removePlaceholders is not None:
            print("A remove placeholder is detected..")
            for name, removePlaceholder in self.library.removePlaceholders.items():
                print(f"Removing placeholder {name}..")
                self.remove_placeholder(removePlaceholder)

        # Check add placeholders
        if self.library.addPlaceholders is not None:
            print("An add placeholder is detected..")
            for name, addPlaceholder in self.library.addPlaceholders.items():
                print(f"Adding placeholder {name}..")
                self.add_placeholder(addPlaceholder)

    def remove_connector(self, removeConnector: RemoveConnector):
        print("Searching the parent element to remove a connector")
        device_type = self.root.find(".//DeviceType")
        if device_type is not None:
            print("Found the device type element")
            connectors = device_type.findall(".//Connector")
            for connector in connectors:
                if connector.attrib["interface"] == removeConnector.interface:
                    device_type.remove(connector)
                    print(f"Removed a connector successfully : {removeConnector.interface}")
        else:
            print("Could not find the device type element")

    def add_connector(self, addConnector: AddConnector):
        print("Searching the parent element to add a connector")
        device_type = self.root.find(".//DeviceType")
        if device_type is not None:
            print("Found the device type element")

            ET.SubElement(device_type, "Connector", {
                "moduleType" : addConnector.moduleType,
                "interface" : addConnector.interface,
                "connectorId" : addConnector.connectorId
            })
            print(f"Added a connector successfully : {addConnector.interface}")
        else:
            print("Could not find the device type element")

    def remove_device(self, removeDevice: RemoveDevice):
        print("Searching the parent element to remove a device")
        device_type = self.root.find(".//DeviceType")
        if device_type is not None:
            print("Found the device type element")
            identifications = device_type.findall(".//DeviceIdentification")
            for identification in identifications:
                id = identification.find(".//Id")
                if id is not None and id.text == removeDevice.id:
                    device_type.remove(identification)
                    print(f"Removed a device successfully : {removeDevice.id}")
        else:
            print("Could not find the device type element")

    def add_device(self, addDevice: AddDevice):
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

            print(f"Added a device successfully : {addDevice.id}")

    def add_placeholder(self, addPlaceholder: AddPlaceholder):
        print("Searching the parent element to add a placeholder")
        libraries = self.root.find(".//Libraries")
        if libraries is not None:
            redirections = libraries.find(".//PlaceholderRedirections")
            if redirections is not None:
                placeholder = ET.SubElement(redirections, "PlaceholderRedirection", {
                    "Placeholder" : addPlaceholder.placeholder,
                    "Redirection" : addPlaceholder.redirection
                })
                print(f"Added a placeholder successfully : {addPlaceholder.placeholder}")
            else:
                print("Could not find the PlaceholderRedirections element")
        else:
            print("Could not find the Libraries element")

    def remove_placeholder(self, removePlaceholder: RemovePlaceholder):
        print("Searching the parent element to remove a placeholder")
        libraries = self.root.find(".//Libraries")
        if libraries is not None:
            redirections = libraries.find(".//PlaceholderRedirections")
            if redirections is not None:
                placeholders = redirections.findall(".//PlaceholderRedirection")
                for placeholder in placeholders:
                    if placeholder.attrib["Placeholder"] == removePlaceholder.placeholder:
                        placeholders.remove(placeholder)
                        print(f"Removed a placeholder successfully : {removePlaceholder.placeholder}")
            else:
                print("Could not find the PlaceholderRedirections element")
        else:
            print("Could not find the Libraries element")

    def add_library(self, addLibrary: AddLibrary):
        print("Searching the parent element to add a library")
        libraries = self.root.find(".//Libraries")
        if libraries is not None:
            library = ET.SubElement(libraries, "Library", {
                "Name": addLibrary.name,
                "Namespace": addLibrary.nameSpace,
                "HideWhenReferencedAsDependency": addLibrary.hideWhenReferencedAsDependency,
                "PublishSymbolsInContainer": addLibrary.publishSymbolsInContainer,
                "SystemLibrary": addLibrary.systemLibrary,
                "LinkAllContent": addLibrary.linkAllContent,
                "DefaultResolution": addLibrary.defaultResolution
            })
            print(f"Added a library successfully : {addLibrary.name}")
        else:
            print("Could not find the Libraries element")

    def remove_library(self, removeLibrary: RemoveLibrary):
        print("Searching the parent element to remove a library")
        libraries_element = self.root.find(".//Libraries")
        if libraries_element is not None:
            libraries = libraries_element.findall(".//Library")
            for library in libraries:
                if library.attrib["Namespace"] == removeLibrary.nameSpace:
                    libraries_element.remove(library)
                    print(f"Removed a library successfully : {removeLibrary.nameSpace}")
        else:
            print("Could not find the Libraries element")

    def save_xml_file(self, path):
        self.tree.write(path, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    import Util
    test_argument_path = "test_arguments.json"
    sample_xml_path = "test_project.xml"
    output_xml_path = "test_project_output.xml"


    test_argument = Util.get_arguments_instance(test_argument_path)

    # create a xml handler with test arguments
    handler = XMLHandler(path=sample_xml_path, library=test_argument.library, deviceDescription=test_argument.deviceDescription)

    # manipulate the xml file according to the arguments
    handler.process()

    # save the manipulated xml
    handler.save_xml_file(output_xml_path)


