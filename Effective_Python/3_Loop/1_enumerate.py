from random import randint

random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i

print(random_bits)
print(bin(random_bits))

flavor_list = ["바닐라", "초콜릿", "피칸", "딸기"]
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f"{i + 1}: {flavor}")

for i, flavor in enumerate(flavor_list):
    print(f"{i + 1}: {flavor}")

it = enumerate(flavor_list)
print(next(it))
print(next(it))

names = ["Cecilia", "남궁민수", "Drake"]
counts = [len(n) for n in names]
print(counts)

longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)
print(max_count)

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)
print(max_count)

for package in zip(names, counts):
    print(package)

names.append("Rosalind")
for package in zip(names, counts):
    print(package)

# for name, count in zip(names, counts, strict=True):
#     print(package)

a = 4
b = 9

for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print("서로소")
        break
else:
    print("서로소 아님")

check = False

for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        check = True
        break

if check:
    print("서로소")
else:
    print("서로소 아님")

for i in range(3):
    print(f"Inside {i=}")
print(f"After {i=}")

# categories = []
# for j, name in enumerate(categories):
#     if name == "리튬":
#         break
# print(j)

my_numbers = [37, 13, 128, 21]
found = [j for j in my_numbers if j % 2 == 0]
print(found)
# print(j)

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        result.append(value/total * 100)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

from pathlib import Path

cwd = Path(__file__)
parent = cwd.parent
data_path = Path.joinpath(parent, "data.txt")

data = read_visits(data_path)
result = normalize(data)
print(result)

def normalize_copy(numbers):
    copied_numbers = list(numbers)
    total = sum(copied_numbers)
    result = []
    for value in copied_numbers:
        result.append(value/total * 100)
    return result

data = read_visits(data_path)
result = normalize_copy(data)
print(result)

class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

read = ReadVisits(data_path=data_path)
result = normalize(read)
print(result)