import math

def isPP(n):
    candidates = []
    result = []
    for i in range(1 + 1, n):
        if (n % i == 0):
            candidates.append(i)

    print(f"Candidates : {candidates}")

    for i in candidates:
        value = math.log(n, i)
        value = round(value, 5)
        if (value % 1 == 0):
            result.append([i, int(value)])

    if len(result) == 0:
        return None
    elif len(result) == 1:
        return result[0]
    else:
        return result

def isPP2(n):
    result = []

    max_b = int(math.log2(n)) + 1

    for b in range(2, max_b + 1):
        a = round(pow(n, (1 / b)))

        if a > 1 and pow(a, b) == n:
            result.append([a, b])

    if not result:
        return None
    elif len(result) == 1:
        return result[0]
    else:
        return result

if __name__ == "__main__":
    print(isPP(4))
    print(isPP(9))
    print(isPP(8))
    print(isPP(32))
    print(isPP(125))
    print(isPP(5))
    print(isPP(81))
