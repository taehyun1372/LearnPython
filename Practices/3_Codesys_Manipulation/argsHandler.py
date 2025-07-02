import json
from typing import Optional, Dict, List
from dataclasses import dataclass, asdict

@dataclass
class Files:
    projectPath: str
    projectName: str
    newProjectName : Optional[str] = "_Virtual"
    backupXMLName: Optional[str] = "_Backup"
    editedXMLName: Optional[str] = "_Edited"
    codesysPath : Optional[str] = r"C:\Program Files (x86)\CODESYS 3.5.20.50\CODESYS\Common"
    codesysVersion : Optional[str] = "CODESYS V3.5 SP20 Patch 5"
    ironPythonScript : Optional[str] = "codesysHandler.py"

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
class RemoveDevice:
    id: str

@dataclass
class RemoveConnector:
    interface: str

@dataclass
class DeviceDescription:
    addDevice: Optional[AddDevice] = None
    addConnector: Optional[AddConnector] = None
    removeDevice: Optional[RemoveDevice] = None
    removeConnector: Optional[RemoveConnector] = None

@dataclass
class AddLibrary:
    name: str
    namespace: str
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
    namespace: str

@dataclass
class RemovePlaceholder:
    placeholder: str

@dataclass
class Library:
    addLibraries: Optional[List[AddLibrary]] = None
    addPlaceholders: Optional[List[AddPlaceholder]] = None
    removeLibraries: Optional[List[RemoveLibrary]] = None
    removePlaceholders: Optional[List[RemovePlaceholder]] = None

@dataclass
class Instance:
    ipAddress : str
    id: str
    password: str

@dataclass
class Target:
    deviceName: str
    applicationName: Optional[str] = "Application"
    gatewayIPAddress: Optional[str] = "192.168.121.132"
    gatewayName : Optional[str] = "Gateway-9"
    gatewayPort: Optional[int] = 1217
    instances: Optional[List[Instance]] = None

@dataclass
class Arguments:
    files: Files
    deviceDescription: DeviceDescription
    library: Library
    target: Target

if __name__ == "__main__":
    from dacite import from_dict, Config

    try:
        with open('arguments.json', 'r') as f:
            data = json.load(f)

            # Convert a dictionary data into a class instance for better access in the code
            arguments = from_dict(data_class=Arguments, data=data, config=Config(cast=[Optional]))

            # Generate a json file to check if conversion was successful
            with open("arguments_test.json", "w") as f:
                json.dump(asdict(arguments), f, indent=4)

    except Exception as e:
        print(f"Invalid JSON: {e}")
