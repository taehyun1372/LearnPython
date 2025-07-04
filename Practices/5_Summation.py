def summation(num):
    test = range(num)
    return sum(test)

def alphabet_position(text):
    result = []
    for c in text.lower():
        if isinstance(c, str):
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                result.append(str(ord(c) - ord('a') + 1))
    return ' '.join(result)



print(summation(5))

letter = 'c'
number = ord(letter) - ord('a') + 1
print(number)

Input = "The sunset sets at twelve o' clock."
print(alphabet_position(Input))

