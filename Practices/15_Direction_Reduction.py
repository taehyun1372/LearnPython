def dir_reduc(arr):
    flag = True

    while(flag):
        temp = []
        flag = False
        for i in arr:
            if arr[i] == "NORTH" and arr[i + 1] == "SOUTH":
                flag = True
                continue
            elif arr[i] == "SOUTH" and arr[i + 1] == "NORTH":
                flag = True
                continue
            elif arr[i] == "WEST" and arr[i + 1] == "EAST":
                flag = True
                continue
            elif arr[i] == "EAST" and arr[i + 1] == "WEST":
                flag = True
                continue
            temp.append(arr[i])
        arr = temp
    return arr

if __name__ == "__main__":
    testee1 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    testee2 = ["NORTH", "WEST", "SOUTH", "EAST"]
    testee3 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    testee4 = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"]
    testee5 = ["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"]

    print(dir_reduc(testee1))
    print(dir_reduc(testee2))
    print(dir_reduc(testee3))
    print(dir_reduc(testee4))
    print(dir_reduc(testee5))
