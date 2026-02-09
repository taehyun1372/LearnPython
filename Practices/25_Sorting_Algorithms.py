def bubble_sorting(arr):
    end = len(arr) - 1
    for i in range(len(arr) - 1):
        for j in range(end, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

def selection_sorting(arr):
    n = len(arr) - 1
    for sorted_index in range(n):
        min_index = n
        for i in range(n, sorted_index, - 1):
            if arr[min_index] > arr[i]:
                min_index = i
        if arr[sorted_index] > arr[min_index]:
            arr[sorted_index], arr[min_index] =  arr[min_index], arr[sorted_index]
    return arr

if __name__ == "__main__":
    test_case1 = [
        91, 23, 45, 67, 12, 89, 34, 56, 78, 90,
        11, 44, 55, 66, 77, 88, 99, 100, 2, 3,
        5, 8, 13, 21, 34, 55, 1, 144, 233, 377
    ]
    print(bubble_sorting(test_case1))

    test_case1 = [
        91, 23, 45, 67, 12, 89, 34, 56, 78, 90,
        11, 44, 55, 66, 77, 88, 99, 100, 2, 3,
        5, 8, 13, 21, 34, 55, 1, 144, 233, 377
    ]
    print(selection_sorting(test_case1))


