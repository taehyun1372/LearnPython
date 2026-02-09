def first_non_repeating_letter(s):
    for i, c in enumerate(s):
        result = s.lower().count(c.lower())
        if result == 1:
            return c
    return ""

if __name__ == "__main__":
    testee1 = "a"
    print(first_non_repeating_letter(testee1))

    testee2 = "stress"
    print(first_non_repeating_letter(testee2))

    testee3 = "moonmen"
    print(first_non_repeating_letter(testee3))

    testee4 = "sTreSS"
    print(first_non_repeating_letter(testee4))



