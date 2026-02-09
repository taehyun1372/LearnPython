def max_sequence(arr):
    maximum = 0

    for i in range(len(arr)):
        if arr[i] <= 0: continue
        total = 0
        for j in range(i, len(arr), 1):
            total += arr[j]
            if (total > maximum): maximum = total

    return maximum

if __name__ == "__main__":
    testee1 =  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = max_sequence(testee1)
    print(result1)

    # testee2 = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
    # result2 = max_sequence(testee2)
    # print(result2)

    testee2 = [10, 20, 15, 17, 25]
    print(max(testee2))


def find_nb(m):
    total = 0
    n = 1
    while (True):
        total += (n * n * n)
        if total == m:
            return n
        elif total > m:
            return -1
        else:
            n += 1
