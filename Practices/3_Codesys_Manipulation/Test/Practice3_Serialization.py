import json
import base64
import subprocess
from typing import Optional, Dict
from dataclasses import dataclass, asdict

@dataclass
class AddDevice:
    id: str
    version: str
    type: str

def to_dict(obj):
    if hasattr(obj, "__dict__"):
        return {k: to_dict(v) for k, v in obj.__dict__.items()}
    elif isinstance(obj, list):
        return [to_dict(x) for x in obj]
    else:
        return obj


arguments = AddDevice("3110", "3.1.1.0", "analog")
with open("temp.json", "w") as f:
    json.dump(to_dict(arguments), f, indent=2)
