def longest_consec(strarr, k):
    if strarr.count == 0: return ""
    maxIndex = 0
    maxString = ""

    for i in range(0, len(strarr) - (k - 1), 1):
        temp = ""
        for j in range(k):
            temp += strarr[i + j]

        if len(temp) > len(maxString):
            maxIndex = i
            maxString = temp

    return maxString



if __name__ == "__main__":
    testee1 = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
    testee2 = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
    testee3 = ["zone", "abigail", "theta", "form", "libe", "zas"]
    result1 = longest_consec(testee1, 2)
    result2 = longest_consec(testee2, 1)
    result3 = longest_consec(testee3, 2)
    print(result1)
    print(result2)
    print(result3)