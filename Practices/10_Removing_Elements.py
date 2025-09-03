input1= [1, 2, 3, 4, 5]

result1 = [input1[i] for i in range(len(input1)) if i % 2 == 0]
for i in result1:
    print(i)