import xml.etree.ElementTree as ET
from os import device_encoding
from re import search

VIRTUAL_CONTROL_ID = "0000 1007"
VIRTUAL_CONTROL_VERSION = "4.16.0.0"
VIRTUAL_CONTROL_TYPE = "4096"
ABINGDON_CONTROLLER_ID = "175c 0001"
ABINGDON_CONTROLLER_VERSION = "3.5.16.0"
ABINGDON_CONTROLLER_TYPE = "4096"
MODBUSFB_PLACEHOLDER = "ModbusFB"
MODBUSFB_REDIRECTION = "ModbusFB, 4.4.0.0 (CODESYS)"

class Project:
    def __init__(self, path):

        ET.register_namespace('', "http://www.w3.org/1999/xhtml")

        self.libraries_element = None
        self.placeholder_element = None
        self.device_type_element = None
        self.device_identification = None
        self.device_connectors = []
        self.libraries = []
        self.placeholders = []

        # Load the XML file
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()
        self.strip_namespaces(self.root)

        self.initialise_devices()

        self.initialize_libraries()

    def strip_namespaces(self, root):
        """Recursively remove all namespaces from XML element tags."""
        for el in root.iter():
            if '}' in el.tag:
                el.tag = el.tag.split('}', 1)[1]
            # Also strip attribute namespaces if needed
            el.attrib = {k.split('}', 1)[-1] if '}' in k else k: v for k, v in el.attrib.items()}

    def convert_abingdon_to_virtual_device(self):
        project.remove_device_identification_by_id(ABINGDON_CONTROLLER_ID)

        project.add_device_identification(DeviceIdentification(
            type=VIRTUAL_CONTROL_TYPE,
            id=VIRTUAL_CONTROL_ID,
            version=VIRTUAL_CONTROL_VERSION
        ))

    def convert_virtual_to_abingdon_device(self):
        project.remove_device_identification_by_id(VIRTUAL_CONTROL_ID)

        project.add_device_identification(DeviceIdentification(
            type=ABINGDON_CONTROLLER_TYPE,
            id=ABINGDON_CONTROLLER_ID,
            version=ABINGDON_CONTROLLER_VERSION
        ))

    def search_device_type_element(self):
        print("Searching the libraries element")
        device_type = self.root.find(".//DeviceType")
        if device_type is not None:
            self.device_type_element = device_type
            print("Found the device type element")

    def initialise_devices(self):
        print("Initializing Devices")

        self.search_device_type_element()

        if self.device_type_element is not None:
            connectors = self.device_type_element.findall(".//Connector")
            for connector in connectors:
                self.device_connectors.append(connector)

            identification = self.device_type_element.find(".//DeviceIdentification")
            self.device_identification = identification

    def remove_device_connector_by_interface(self, interface):
        for connector in self.device_connectors:
            if connector.attrib["interface"] == interface:
                self.device_type_element.remove(connector)

    def add_device_connector(self, device_connector):
        ET.SubElement(self.device_type_element, "Connector", {
            "moduleType" : device_connector.moduleType,
            "interface" : device_connector.interface,
            "connectorId" : device_connector.connectorId
        })

    def remove_device_identification_by_id(self, id):
        if self.device_type_element is not None:
            if self.device_identification is not None:
                id_element = self.device_identification.find(".//Id")
                if id_element is not None and id_element.text == id:
                    self.device_type_element.remove(self.device_identification)

    def add_device_identification(self, device_identification):
        identification_element = ET.SubElement(self.device_type_element, "DeviceIdentification")

        type = ET.SubElement(identification_element, "Type")
        type.text = device_identification.type

        id = ET.SubElement(identification_element, "Id")
        id.text = device_identification.id

        version = ET.SubElement(identification_element, "Version")
        version.text = device_identification.version

    def search_libraries_element(self):
        print("Searching the libraries element")
        libraries_element = self.root.find(".//Libraries")
        if libraries_element is not None:
            self.libraries_element = libraries_element
            print("Found the libraries element")

        placeholder_element = self.root.find(".//PlaceholderRedirections")
        if placeholder_element is not None:
            self.placeholder_element = placeholder_element
            print("Found the placeholder element")


    def initialize_libraries(self):
        print("Initializing Libraries")

        self.search_libraries_element()

        if self.libraries_element is not None:
            libraries = self.libraries_element.findall(".//Library")
            for library in libraries:
                self.libraries.append(library)

        if self.placeholder_element is not None:
            placeholders = self.placeholder_element.findall(".//PlaceholderRedirection")
            for placeholder in placeholders:
                self.placeholders.append(placeholder)

    def add_placeholder(self, placeholder):
        if self.placeholder_element is not None:
            placeholder = ET.SubElement(self.placeholder_element, "PlaceholderRedirection", {
                "Placeholder" : placeholder.Placeholder,
                "Redirection" : placeholder.Redirection
            })
            self.placeholders.append(placeholder)

    def remove_placeholder_by_placeholder(self, placeholder):
        if self.placeholder_element is not None:
            for placeholder in self.placeholders:
                if placeholder.attrib["Placeholder"] == placeholder:
                    self.placeholder_element.remove(placeholder)

    def display_libraries(self):
        for library in self.libraries:
            print(library.attrib["Name"])

    def add_library(self, library):
        if self.libraries_element is not None:
            library = ET.SubElement(self.libraries_element, "Library", {
                "Name" : library.Name,
                "Namespace" : library.NameSpace,
                "HideWhenReferencedAsDependency" : library.HideWhenReferencedAsDependency,
                "PublishSymbolsInContainer" : library.PublishSymbolsInContainer,
                "SystemLibrary" : library.SystemLibrary,
                "LinkAllContent" : library.LinkAllContent,
                "DefaultResolution" : library.DefaultResolution
            })
            self.libraries.append(library)

    def remove_library_by_namespace(self, namespace):
        if self.libraries_element is not None:
            for library in self.libraries:
                if library.attrib["Namespace"] == namespace:
                    self.libraries_element.remove(library)

    def save_xml_file(self, path):
        self.tree.write(path, encoding="utf-8", xml_declaration=True)

class Library:
    def __init__(self, Name, NameSpace, HideWhenReferencedAsDependency, PublishSymbolsInContainer, SystemLibrary, LinkAllContent, DefaultResolution):
        self.Name = Name
        self.NameSpace = NameSpace
        self.HideWhenReferencedAsDependency = HideWhenReferencedAsDependency
        self.PublishSymbolsInContainer = PublishSymbolsInContainer
        self.SystemLibrary = SystemLibrary
        self.LinkAllContent = LinkAllContent
        self.DefaultResolution = DefaultResolution

class Placeholder:
    def __init__(self, Placeholder, Redirection):
        self.Placeholder = Placeholder
        self.Redirection = Redirection

class DeviceConnector:
    def __init__(self, moduleType, interface, connectorId):
        self.moduleType = moduleType
        self.interface = interface
        self.connectorId= connectorId

class DeviceIdentification:
    def __init__(self, type, id, version):
        self.type = type
        self.id = id
        self.version = version

if __name__ == "__main__":
    print("Hello World")
    # Open a xml file
    project = Project("Modbus_Test_Project.xml")

    # Change Device
    project.remove_device_connector_by_interface("GPIOSysfs")

    project.convert_abingdon_to_virtual_device()

    # Add a library
    project.add_library( Library(
        Name="#ModbusFB",
        NameSpace="ModbusFB",
        HideWhenReferencedAsDependency="false",
        PublishSymbolsInContainer="false",
        SystemLibrary="false",
        LinkAllContent="false",
        DefaultResolution="ModbusFB, * (CODESYS)"
    ))

    project.add_placeholder(Placeholder(
        Placeholder = MODBUSFB_PLACEHOLDER,
        Redirection = MODBUSFB_REDIRECTION
    ))

    project.display_libraries()

    # save xml file
    project.save_xml_file("Modbus_Test_Project_Edited.xml")


