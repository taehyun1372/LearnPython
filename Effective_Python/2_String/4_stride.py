x = ["red", "orange", "yellow", "green", "blue", "purple"]
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

x = b"mongoose"
y = x[::-1]
print(y)

x = "한글"
y=x[::-1]
print(y)

x = "한글".encode("utf-8")
print(x)
y = x[::-1]
print(y)
# z = y.decode("utf-8")

x = "abc123++".encode("utf-8")
print(x)
y = x[::-1]
print(y)
print(y.decode("utf-8"))

#shallow copy 
a = [1, 2]
b = a.copy()
print(a)
print(b)
assert a == b and a is not b

a = [[1, 2], [3, 4]]
b = a.copy()
print(a)
print(b)
assert a == b and a is not b
a[0].append(99)
print(a)
print(b)

from copy import deepcopy
#deep copy
a = [[1, 2], [3, 4]]
b = deepcopy(a)
print(a)
print(b)
assert a == b and a is not b
a[0].append(99)
print(a)
print(b)