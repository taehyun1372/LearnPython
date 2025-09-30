import pprint
from copy import copy as shallow_copy

def reveal_vars(*names):
    print(f"{'Variable':>10}{'Value':>10}{'Address':>20}")
    print("-" * 40)
    for name in names:
        value = globals().get(name, None)
        print(f"{name:>10}{value!s:>10}{hex(id(value)):>20}")
    print()

tuple1 = (42, "John", 3.14)
tuple2 = (42, "Mike", {"Python", "Data Science"})

for item in tuple1:
    print(item)

# tuple1[0] = 12

print(hash(tuple1))
# print(hash(tuple2))

a = 42
b = a

reveal_vars("a", "b")

a = 43
reveal_vars("a", "b")

inventory = {
    "fruits": {
        "apple": 50,
        "banana": 30,
    },
    "dairy": {
        "cheese": 15,
        "milk": 20,
    }
}

backup = shallow_copy(inventory)

pprint.pp(backup, width=50)
pprint.pp(inventory, width=50)
