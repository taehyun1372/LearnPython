def custom_product(*lists):
    lenthes = []
    for item in lists:
        lenthes.append(len(item))

    for i, length in enumerate(lenthes):
        for j in range(length):
            print(i, j)

result = custom_product([1, 2], ["a", "b"], ["one", "two"])
print(result)



def sub_iteration(list, count=0, result=[]):
    if count < len(list):
        result.append(list[count])
        count += 1
        sub_iteration(list, count, result)
    return result

result = sub_iteration([1,2,3,4,5])
print(result)

# sub iteration 
# input list_a list_b list_c
# output (list_a[0], list_b[0], list_c[0]), (list_a[0], list_b[0], list_c[1], ..)

def iterate_all(lists, index=None, result=None):
    if not index:
        index = []
        for i, j in enumerate(lists):
            index.append(i, 0)
    if not result: result = []
    temp = []
    for i, j in index:
        temp.append(lists[i][j])

        
