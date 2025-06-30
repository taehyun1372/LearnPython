import json

class SimpleNamespace(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def to_namespace(obj):
    if isinstance(obj, dict):
        return SimpleNamespace(**{k: to_namespace(v) for k, v in obj.items()})
    elif isinstance(obj, list):
        return [to_namespace(x) for x in obj]
    else:
        return obj

# Load JSON from file
with open(r"C:\Users\a00533064\OneDrive - ONEVIRTUALOFFICE\Desktop\Code\LearnPython\Practices\3_Codesys_Manipulation\Test\temp.json", "r") as f:
    raw_data = json.load(f)

arguments = to_namespace(raw_data)

print(arguments.id)         # "project1"
print(arguments.version)    # "my_path"
