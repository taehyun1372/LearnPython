my_dict = {"빨강": 1, "파랑": 2, "초록": 3}
for key in my_dict:
    if key == "파랑":
        pass
        # my_dict["노랑"] = 4

for key in my_dict:
    if key == "파랑":
        pass
        # del my_dict["초록"]

for key in my_dict:
    if key == "파랑":
        my_dict["초록"] = 4

my_set = {"빨강", "파랑", "초록"}
for color in my_set:
    if color == "파랑":
        pass
        # my_set.add("노랑")

my_list = [1, 2, 3]
for number in my_list:
    print(number)
    if number == 2:
        my_list[0] = -1

print(my_list)

# my_list = [1, 2, 3]
# for number in my_list:
#     print(number)
#     if number == 2:
#         my_list.insert(0, 4)


for number in my_list:
    print(number)
    if number == 2:
        my_list.insert(3, 4)

print(my_list)

keys_copied = list(my_dict.keys())
for key in keys_copied:
    if key == "파랑":
        my_dict["초록"] = 40

print(my_dict)

set_copied = set(my_set)
for item in set_copied:
    if item == "파랑":
        my_set.add("노랑")

print(my_set)

my_dict = {"빨강": 1, "파랑": 2, "초록": 3}
modifications = {}
for key in my_dict:
    if key == "파랑":
        modifications["초록"] = 100
my_dict.update(modifications)
print(my_dict)

for k, v in my_dict.items():
    if k == "파랑":
        modifications["초록"] = 4
    if v == 4:
        modifications["노랑"] = 5
my_dict.update(modifications)
print(my_dict)


for k, v in my_dict.items():
    if k == "파랑":
        modifications["초록"] = 4
    other_value = modifications.get(k)
    if v == 4 or other_value == 4:
        modifications["노랑"] = 5
my_dict.update(modifications)
print(my_dict)