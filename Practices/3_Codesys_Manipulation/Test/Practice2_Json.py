import json
from typing import Optional, Dict
from dataclasses import dataclass

try:
    with open('sample.json', 'r') as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")

if (data is not None):
    for key, value in data.items():
        print(f"Key is  {key}")
        print(f"Value is  {value}")

@dataclass
class Project:
    name: str
    date: str
    description : Optional[str] = "Default Description"

@dataclass
class User:
    name: str
    projects : Dict[str, Project]
    age : Optional[int] = 30

projects_dict = {k: Project(**v) for k, v in data["projects"].items()}
data["projects"] = projects_dict
user = User(**data)


print(f"user name is {user.name}")
print(f"user age is {user.age}")
for key, project in user.projects.items():
    print(f"{key} :{project.name}, {project.date}, {project.description}")
