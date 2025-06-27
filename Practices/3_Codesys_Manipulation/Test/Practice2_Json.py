import json
from typing import Optional, Dict
from dataclasses import dataclass
from dacite import from_dict, Config

try:
    with open('sample.json', 'r') as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")

@dataclass
class Project:
    name: str
    date: str
    description : Optional[str] = "Default Description"

@dataclass
class Education:
    university : str
    period : int

@dataclass
class User:
    name: str
    age: int
    education: Education
    projects : Dict[str, Project]

projects_dict = {k: Project(**v) for k, v in data["projects"].items()}

education = Education(**data["education"])

data["projects"] = projects_dict
data["education"] = education

user = User(**data)

print(user.age)
print(user.education.university)

user2 = from_dict(data_class=User, data=data, config=Config(cast=[Optional]))

print(user2.education.university)

print(f"user name is {user.name}")
print(f"user age is {user.age}")
for key, project in user.projects.items():
    print(f"{key} :{project.name}, {project.date}, {project.description}")
