def valid_ISBN10(isbn):
    if len(isbn) is not 10: return False

    if isbn.find("X") is not -1 and isbn.find("X") is not 9: return False

    sum = 0
    for i, v in enumerate(isbn):
        if v == "X" : sum += 10 * (i + 1)
        elif str.isdigit(v) : sum += int(v) * (i + 1)
        else : return False
    return True if sum % 11 == 0 else False

testee1 = "1112223339"
testee2 = "048665088X"
testee3 = "1293000000"

print(valid_ISBN10(testee1))
print(valid_ISBN10(testee2))
print(valid_ISBN10(testee3))
