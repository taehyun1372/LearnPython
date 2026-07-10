def going(n):
    sum = 1
    operator = 1/n
    for i in range(n - 1, 0, -1):
        sum = sum + operator
        operator = operator * (1 / i)
    return sum

def factorial(n):
    result = 1
    for i in range(1, n + 1, 1):
        result = result * i
    return result

if __name__ == '__main__':
    print(going(5))
