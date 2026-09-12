i = 3
x = "even" if i % 2 == 0 else "odd"
print(x)

def fail():
    raise Exception("이런!")

x = fail() if False else 20
print(x)

result = [x/4 for x in range(10) if x%2==0]
print(result)

result = [x for x in range(100)]
print(result)

result = [str(x) for x in range(100) if x%10==0]
print(result)

