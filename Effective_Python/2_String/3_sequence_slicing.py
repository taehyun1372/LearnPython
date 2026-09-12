a = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:-1])
print(a[-3:-1])

first_twenty_items = a[:20]
print(first_twenty_items)

last_twenty_items = a[-20:]
print(last_twenty_items)

b = a[3:]
print("Before ", b)
b[1] = 99
print("After ", b)
print("No change ",a)

print("Before ", a)
a[2:7] = [99, 22, 14]
print("After ", a)

print("Before ", a)
a[2:3] = [47, 11]
print("After ", a)

b = a[:]
assert b == a and b is not a

b = a
print("Before a", a)
print("Before b", b)
a[:] = [101, 102, 103]
print("After a", a)
print("After b", b)
print(a is b)
