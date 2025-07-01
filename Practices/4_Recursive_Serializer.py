class Person:
    def __init__(self):
        self.name = "Alice"
        self.age = 30
        self.project = Project()
        self.books = {"art": Book(12, 22), "economy": Book(56, 66)}
        self.items = []
        self.items.append(Item(6, "I like it"))
        self.items.append(Item(2, "I rarely use it"))

class Project:
    def __init__(self):
        self.level = "High"
        self.cost = "Low"

class Book:
    def __init__(self, age, page):
        self.age = age
        self.page = page

class Item:
    def __init__(self, size, description):
        self.size = size
        self.description = description

class Empty:
    pass

def to_dict(obj):
    result = {}
    print(f"Object {obj} has been passed")
    if hasattr(obj, "__dict__"):
        for key, val in obj.__dict__.items():
            result[key] = to_dict(val)
        return result
    elif isinstance(obj, dict):
        for key, val in obj.items():
            result[key] = to_dict(val)
        return result
    elif isinstance(obj, list):
        return [to_dict(item) for item in obj]
    else:
        return obj

class ToObj:
    def __init__(self, dic):
        for key, val in dic.items():
            if isinstance(val ,dict):
                val = ToObj(val)
            elif isinstance(val, list):
                val = [ToObj(i) for i in val]
            setattr(self, key, val)

# Serialization
roy = Person()
# mike = Empty()
result = to_dict(roy)
# to_dict(mike)
# to_dict(dict)
print(result)

# Deserialization
dic = {"project": "serious", "resource": "critical", "items": {"book": "modern art", "fork": "for cook"}, "projects": [{"big": 2024}, {"enormous": 2023}, {"mere": 2022}]}
obj = ToObj(dic)
print(obj)
print(obj.items.book)