import base64

data = "test result"

raw = data.encode("ascii")
print(raw)
print(list(raw))

encoded = base64.b64encode(raw)
print(encoded)
print(list(encoded))