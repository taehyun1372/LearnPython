import random

def flip_coin():
    if random.randint(0, 1) == 0:
        return "Front"
    else:
        return "Back"

def flip_is_heads():
    print("let's try!")
    return flip_coin() == "Front"

# flips = [flip_is_heads() for _ in range(5)]
# print(flips)
# all_heads = False not in flips
# print(all_heads)

all_heads = True
for _ in range(5):
    if not flip_is_heads():
        all_heads = False
        break

print(all_heads)

print(all([0, 1, "True", 1.1]))
print(all([1, "True", True]))
print(True and 1 and 0)
print(1 and 2 and 3)

all_heads = all(flip_is_heads() for _ in range(5))