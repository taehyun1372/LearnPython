myList1 = [1, 2, 3, 4]
myList2 = [1, 2, 3, 4]
myList3 = [1, 2, 3, 4]

newList1 = myList1
newList1[0] = 991
print(myList1)

newList2 = myList2[:]
newList2[0] = 992
print(myList2)

newList3 = list(myList3)
newList3[0] = 993
print(myList3)

