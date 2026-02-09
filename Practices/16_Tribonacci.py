def tribonacci(signature, n):
    if n == 0: return []
    if len(signature) > n: return signature[:n]
    for i in range(n - len(signature)):
        signature.append(signature[-1] + signature[-2] + signature[-3])
    return signature

if __name__ == "__main__":
    testee1 = [1,1,1]
    result1 = tribonacci(testee1, 10)
    print(result1)

    testee2 = [1, 1, 1]
    result2 = tribonacci(testee2, 1)
    print(result2)

    testee3 = [100, 120, 200]
    result3 = tribonacci(testee3, 0)
    print(result3)
    print("Hello, World")