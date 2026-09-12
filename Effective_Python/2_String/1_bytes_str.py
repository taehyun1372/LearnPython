a = b"h\x65llo"

print(type(a))
print(list(a))
print(a)

a = "a\u0300 propos"
print(type(a))
print(list(a))
print(a)

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    elif isinstance(bytes_or_str, str):
        value = bytes_or_str
    else:
        raise TypeError("input should be bytes or str")
    return value

print(type(to_str(b'foo')))
print(to_str(b'foo'))
print(type(to_str("bar")))
print(to_str("bar"))
print(type(to_str(b"\xed\x95\x9c")))
print(to_str(b"\xed\x95\x9c"))

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    elif isinstance(bytes_or_str, bytes):
        value = bytes_or_str
    else:
        raise TypeError("input type should be str or bytes")
    return value

print(type(to_bytes(b'foo')))
print(to_bytes(b'foo'))
print(type(to_bytes("bar")))
print(to_bytes("bar"))
print(type(to_bytes("한글")))
print(to_bytes("한글"))

blue_bytes = b'blue'
blue_str = "blue"
print(b"red %s" % blue_bytes)
print("red %s" % blue_str)

mix = "red %s" % blue_bytes
print(mix)
print(type(mix))
print(list(mix))

# with open("Effective_Python\\2_String\\data.bin", "w") as f:
#     f.write(b"\xf1\xf2\xf3\xf4\xf5")

with open("Effective_Python\\2_String\\data.bin", "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")


with open("Effective_Python\\2_String\\data.bin", "rb") as f:
    data = f.read()

a = 0b10111011
b = 0xc5f
print("binary: %d, hex: %d" %(a,b))

key = "my_var"
value = 1.234
formatted = "%-10s = %.2f" %(key, value)
print(formatted)

# reordered_tuple = "%-10s = %.2f" %(value, key)
# reordered_string = "%.2f = %-10s" %(key, value)

pantry = [
    ("아보카도", 1.25),
    ("바나나", 2.5),
    ("체리", 15)
]
for i, (item, count) in enumerate(pantry):
    print("#%d: %-10s = %.2f" % (i, item, count))


for i, (item, count) in enumerate(pantry):
    print("#%d: %-10s = %.2f" % 
        (i + 1,
        item.title(), 
        round(count)))

key = "my_var"
value = 1.234

old_way = "%-10s = %.2f" % (key,value)

new_way = "%(key)-10s = %(value).2f" % {
    "key": key,
    "value": value
}
print(new_way)

reordered = "%(key)-10s = %(value).2f" % {
    "value": value,
    "key": key
}
print(reordered)

a = 1234.5678
formatted = format(a, ",.2f")
print(formatted)

b ="my string"
formatted = format(b, "^20s")
print("*", formatted, "*")

key = "my_var"
value = 1.234
formatted = "{} = {}".format(key, value)
print(formatted)

formatted = "{:10} = {:.2f}".format(key, value)
print(formatted)

print("%.2f%%" % 12.5)
print("{} replaces {{}}".format(1.23))

formatted = "{1} {0}".format(key, value)
print(formatted)

key = "my_var"
value = 1.234

formatted = f"{key} = {value}"
print(formatted)

formatted = f"{key:<10s} = {value:.2f}"
print(formatted)

for i, (item, count) in enumerate(pantry):
    f_string = f"#{i+1}: {item.title():<10s} = {round(count)}"
    print(f_string)

