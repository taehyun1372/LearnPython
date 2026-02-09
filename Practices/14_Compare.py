def comp(array1, array2):
    if array1 == None or array2 == None: return False

    for i in array2:

        flag = False
        for j in array1:
            temp = j

            while(temp <= i):
                if (temp == i):
                    flag = True
                    break
                temp = temp * j

        if not flag: return False
    return True

if __name__ == "__main__":
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [121 * 121, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
    result = comp(a1, a2)
    print(result)