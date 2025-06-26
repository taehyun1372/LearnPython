import json
from typing import Optional, Dict
from dataclasses import dataclass

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



if __name__ == "__main__":
    print("Hello world!")
    try:
        with open('Arguments.json', 'r') as f:
            data = json.load(f)

            # Print arguments
            for key, value in data.items():
                print(f"Key is  {key}")
                print(f"Value is  {value}")

            # Target
            instances = data["target"]["instances"]
            if instances is None:
                data["target"]["instances"] = None
            else:
                instance_dict = {k: Instance(**v) for k, v in instances.items()}
                data["target"]["instances"] = instance_dict

            # Library
            removePlaceholders = data["library"]["removePlaceholders"]
            if removePlaceholders is None:
                data["library"]["removePlaceholders"] = None
            else:
                removePlaceholders_dict = {k: RemovePlaceholder(**v) for k, v in removePlaceholders.items()}
                data["library"]["removePlaceholders"] = removePlaceholders_dict

            removeLibraries = data["library"]["removeLibraries"]
            if removeLibraries is None:
                data["library"]["removeLibraries"] = None
            else:
                removeLibraries_dict = {k: RemoveLibrary(**v) for k, v in removeLibraries.items()}
                data["library"]["removeLibraries"] = removeLibraries_dict

            addPlaceholders = data["library"]["addPlaceholders"]
            if addPlaceholders is None:
                data["library"]["addPlaceholders"] = None
            else:
                addPlaceholders_dict = {k: AddPlaceholder(**v) for k, v in addPlaceholders.items()}
                data["library"]["addPlaceholders"] = addPlaceholders_dict

            addLibraries = data["library"]["addLibraries"]
            if addLibraries is None:
                data["library"]["addLibraries"] = None
            else:
                addLibraries_dict = {k: AddLibrary(**v) for k, v in addLibraries.items()}
                data["library"]["addLibraries"] = addLibraries_dict

            arguments = Arguments(**data)


    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
