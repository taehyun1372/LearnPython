def increment_string(string):
    if len(string) == 0: return "1"

    index = 0
    found = False

    for i in range(len(string) - 1, -1, -1):
        if string[i].isnumeric():
            index = i
            found = True
        else:
            break

    if found is False:
        return string + "1"
    else:
        literal = string[:index]
        numeric = string[index:]
        return literal + str(int(numeric) + 1).zfill(len(numeric))

if __name__ == "__main__":
    print(increment_string("foo"))
    print(increment_string("foobar001"))
    print(increment_string("foobar1"))
    print(increment_string("foobar00"))
    print(increment_string("foobar99"))
    print(increment_string("foobar099"))
    print(increment_string("fo99obar99"))
    print(increment_string("1234"))
    print(increment_string(""))
