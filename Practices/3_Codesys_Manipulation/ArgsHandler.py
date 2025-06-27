import json
from typing import Optional, Dict
from dataclasses import dataclass, asdict
from dacite import from_dict, Config

@dataclass
class ProjectFile:
    projectFilePath: str
    projectFileName: str
    backupXMLName: Optional[str] = "backup"
    editedXMLName: Optional[str] = "edited"

@dataclass
class RemoveDevice:
    id: str

@dataclass
class RemoveConnector:
    interface: str

@dataclass
class AddDevice:
    id: str
    version: str
    type: str

@dataclass
class AddConnector:
    moduleType : str
    interface: str
    connectorId: str

@dataclass
class DeviceDescription:
    removeDevice: Optional[RemoveDevice] = None
    removeConnector: Optional[RemoveConnector] = None
    addDevice: Optional[AddDevice] = None
    addConnector: Optional[AddConnector] = None

@dataclass
class AddLibrary:
    name: str
    nameSpace: str
    hideWhenReferencedAsDependency: str
    publishSymbolsInContainer: str
    systemLibrary: str
    linkAllContent: str
    defaultResolution: str

@dataclass
class AddPlaceholder:
    placeholder: str
    redirection: str

@dataclass
class RemoveLibrary:
    nameSpace: str

@dataclass
class RemovePlaceholder:
    placeholder: str

@dataclass
class Library:
    addLibraries: Optional[Dict[str, AddLibrary]] = None
    addPlaceholders: Optional[Dict[str, AddPlaceholder]] = None
    removeLibraries: Optional[Dict[str, RemoveLibrary]] = None
    removePlaceholders: Optional[Dict[str, RemovePlaceholder]] = None

@dataclass
class Instance:
    ipAddress : str
    id: str
    password: str

@dataclass
class Target:
    deviceName: Optional[str] = None
    applicationName: Optional[str] = "Application"
    gatewayIPAddress: Optional[str] = "192.168.121.132"
    gatewayPort: Optional[int] = 1217
    instances: Optional[Dict[str, Instance]] = None

@dataclass
class Arguments:
    projectFile: ProjectFile
    deviceDescription: DeviceDescription
    library: Library
    target: Target

def get_arguments_instance():
    try:
        with open('Arguments.json', 'r') as f:
            data = json.load(f)

            # Convert a dictionary data into a class instance for better access in the code
            arguments = from_dict(data_class=Arguments, data=data, config=Config(cast=[Optional]))

            return arguments

    except Exception as e:
        print(f"Invalid JSON: {e}")


if __name__ == "__main__":
    try:
        with open('Arguments.json', 'r') as f:
            data = json.load(f)

            # Convert a dictionary data into a class instance for better access in the code
            arguments = from_dict(data_class=Arguments, data=data, config=Config(cast=[Optional]))

            # Generate a json file to check if conversion was successful
            with open("Arguments_Test.json", "w") as f:
                json.dump(asdict(arguments), f, indent=4)

    except Exception as e:
        print(f"Invalid JSON: {e}")
