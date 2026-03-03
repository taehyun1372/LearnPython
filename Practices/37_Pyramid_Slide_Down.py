def longest_slide_down(pyramid):
    results = []
    sub_slide_down(pyramid, 0, 0, results)
    print(results)
    return max(results)

def sub_slide_down(pyramid, index, result, results):
    for i in pyramid[index]:
        result += i
        if index < len(pyramid) - 2:
            sub_slide_down(pyramid, index + 1 ,result, results)
        else:
            for j in pyramid[index + 1]:
                results.append(result + j)

testee1 = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
testee2 = [[10], [10, 20], [10, 10, 20], [10, 90, 10, 20]]

print(longest_slide_down(testee1))
print(longest_slide_down(testee2))

