def numbers():
    yield 1
    yield 2
    yield 3

result = numbers()

print(next(result))
print(next(result))
print(next(result))
# print(next(result))

def test():
    print("A")
    yield 1

    print("B")
    yield 2

    print("C")
    yield 3

result2 = test()
print(next(result2))
print(next(result2))
print(next(result2))

class MyNumbers:
    def __iter__(self):
        return iter([1, 2, 3])

numbers = MyNumbers()
for number in numbers:
    print(number)

class MyNumbers2:
    def __iter__(self):
        yield 10
        yield 20
        yield 30

numbers2 = MyNumbers2()
for number in numbers2:
    print(number)

class SensorData():
    def __init__(self):
        self.data = [11, 12, 13]

    def __iter__(self):
        return iter(self.data)

sensor = SensorData()
for data in sensor:
    print(data)


def numbers():
    yield 10
    yield 20
    yield 30

gen1 = numbers()
gen2 = numbers()

print(next(gen1))
print(next(gen2))