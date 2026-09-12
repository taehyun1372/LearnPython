import hashlib

data = b"Hello World"
data2 = b"hello World"

hash_value = hashlib.sha256(data).hexdigest()
print(f"Hello world sha256 hash {hash_value}, lengh is {len(hash_value)//2 * 8}")

hash_value2 = hashlib.sha256(data2).hexdigest()
print(f"hello world sha256 hash {hash_value2}, lengh is {len(hash_value2)//2 * 8}")

hash_value3 = hashlib.sha224(data).hexdigest()
print(f"Hello world sha224 hash {hash_value3}, lengh is {len(hash_value3)//2 * 8}")

hash_value4 = hashlib.sha384(data).hexdigest()
print(f"Hello world sha384 hash {hash_value4}, lengh is {len(hash_value4)//2 * 8}")

hash_value5 = hashlib.sha512(data).hexdigest()
print(f"Hello world sha512 hash {hash_value5}, lengh is {len(hash_value5)//2 * 8}")