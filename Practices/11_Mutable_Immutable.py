from operator import truediv

number1 = 314
number2 = number1
print("---The same identity----")
print(id(number1))
print(id(number2))
print(id(314))

number1 = 7
print("----After reassignment---")
print(id(number1))


print("----Boolean identity---")
x = True
y = True
z = False

print(id(x))
print(id(y))
print(id(z))

print("----String identity---")
greeting = "Hello!"
print(id(greeting))

print(id(greeting[0]))
print(id(greeting[1]))
print(id(greeting[2]))

# greeting[1] = 'E'
greeting = "Hello World"
print(id(greeting))
greeting = greeting.upper()
print(greeting)
print(id(greeting))
greeting = greeting.title()
print(greeting)
print(id(greeting))

x = 42
print(id(x))
x = x + 1
print(id(x))

y = [1, "something", False]
print(id(y))
print(type(y))

y.append(1.33)
print(id(y))
print(type(y))