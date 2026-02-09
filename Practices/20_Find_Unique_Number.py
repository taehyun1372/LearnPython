def find_uniq(arr):
    temp1 = None
    temp2 = None
    isTemp1Duplicated = False
    isTemp2Duplicated = False
    for i in range(0, len(arr), 1):
        if temp1 is None:
            temp1 = arr[i]
        elif arr[i] != temp1 and temp2 is None:
            temp2 = arr[i]
        elif arr[i] == temp1:
            isTemp1Duplicated = True
        elif arr[i] == temp2:
            isTemp2Duplicated = True

        if isTemp1Duplicated and temp2 is not None:
            return temp2
        if isTemp2Duplicated and temp1 is not None:
            return temp1


if __name__ == "__main__":
    testee1 = [ 1, 1, 1, 2, 1, 1 ]
    testee2 = [ 0, 0, 0.55, 0, 0 ]
    testee3 = [ 3, 10, 3, 3, 3 ]
    result1 = find_uniq(testee1)
    result2 = find_uniq(testee2)
    result3 = find_uniq(testee3)
    print(result1)
    print(result2)
    print(result3)