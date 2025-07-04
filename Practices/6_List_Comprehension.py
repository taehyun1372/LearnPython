
characters = ['a', 'b', 'c', 'd']
new_characters = [c*3 for c in characters]

items = ["New", "Era", "Might", "Begin"]
new_items = [item.lower() for item in items]

mixed_items = ["Some", 3, "Toys", ' ', {"project": 2}, [1, 2, "Expensive"]]
new_mixed_items = [item.lower() for item in mixed_items if isinstance(item, str)]

numbers = [1,2,3,4,5]
labels = ['even' if x % 2 == 0 else 'odd' for x in numbers]

print(new_characters)
print(new_items)
print(new_mixed_items)
print(labels)


