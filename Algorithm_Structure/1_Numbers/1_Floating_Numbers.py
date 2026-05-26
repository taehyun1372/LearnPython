print(10 / 3)
print(10 // 3)
print(10 % 3)
k, v = divmod(10, 3)
print(k, v)
print(round(1234.5678, -2))
print(round(1234.5678, 2))

print(sum(0.1 for i in range(3)) == 0.3)

print(bin(999))
print(type(bin(999)))
print(bin(999)[1])
print(oct(999))
print(type(oct(999)))

def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    length = len(str(number))
    for i in range(length):
        result += int(str(number)[length - i - 1]) * (base ** i)
    return result

def test_convert_to_decimal():
    number1, base1 = 1001, 2
    number2, base2 = 1100, 3

    assert(convert_to_decimal(number1, base1) == 9)
    assert(convert_to_decimal(number2, base2) == 36)

    print("Test Success")

test_convert_to_decimal()

print(1001 // 10) # 100
print(100 // 10) # 10
print(10 // 10) # 1
print(1 // 10) # 10