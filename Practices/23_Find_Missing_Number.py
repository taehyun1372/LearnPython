
# 3, 4, 6, 0, 2, 1 -> 5
def get_missing_number(arr):
    temp = list(range(0, len(arr) + 1))
    for item in arr:
        temp.remove(item)
    return temp[0]


if __name__ == "__main__":
    print("Something")
    testee1 = [3, 4, 5, 0, 2, 1]
    result1 = get_missing_number(testee1)
    print(result1)