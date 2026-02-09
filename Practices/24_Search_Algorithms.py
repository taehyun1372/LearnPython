class HashTable:
    def __init__(self):
        self._table = [[] for _ in range(13)]
        self._hash_value = 13

    def add(self, element):
        self._table[self.hash_function(element)].append(element)

    def add_array(self, arr):
        for item in arr:
            self.add(item)

    def hash_function(self, element):
        return element % self._hash_value

    def remove(self, element):
        for i in self._table[self.hash_function(element)]:
            if i == element:
                self._table[self.hash_function(element)].remove(element)
                return 1
        return -1

    def search(self, element):
        for index, value in enumerate(self._table[self.hash_function(element)]):
            if value == element:
                return (self.hash_function(element), index)
        return None

    def print_all_elements(self):
        for index, bucket  in enumerate(self._table):
            print(f"bucket index is {index}")
            for element in bucket:
                print(element, end=",")
            print("")

def binary_search(arr, target):
    start = 0
    end = len(arr)
    while (end - start > 0):
        middle = (end - start) // 2 + start
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            end = middle
        elif arr[middle] < target:
            start = middle + 1
    return -1

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    array1 = [4, 7, 1, 9, 3]
    target1 = 1
    print(linear_search(array1, target1))

    array2 = [10, 20, 30, 40]
    target2 = 10
    print(linear_search(array2, target2))

    array3 = [5, 8, 12, 6]
    target3 = 6
    print(linear_search(array3, target3))

    array4 = [2, 4, 6, 8]
    target4 = 5
    print(linear_search(array4, target4))

    array5 = []
    target5 = 3
    print(linear_search(array5, target5))

    array6 = [3, 7, 12, 18, 25, 31, 44, 59, 63, 78, 91, 105, 120]
    target6 = 44
    print(binary_search(array6, target6))

    array7 = [-100, -50, -20, -10, -3, 0, 4, 9, 15, 22, 40]
    target7 = -10
    print(binary_search(array7, target7))

    array8 = list(range(0, 1_000_000, 2))
    target8 = 888_888
    print(binary_search(array8, target8))

    array9 = [9]
    target9 = 10
    print(binary_search(array9, target9))

    array10 = [
     13,  26,  39,  52,  65,  78,  91, 104, 117, 130,
      1,  14,  27,  40,  53,  66,  79,  92, 105, 118,
      2,  15,  28,  41,  54,  67,  80,  93, 106, 119,
      3,  16,  29,  42,  55,  68,  81,  94, 107, 120,
      4,  17,  30,  43,  56,  69,  82,  95, 108, 121,
      5,  18,  31,  44,  57,  70,  83,  96, 109, 122
    ]
    target10 = 83
    hash_table = HashTable()
    hash_table.add_array(array10)
    hash_table.print_all_elements()
    print(hash_table.search(target10))


    print(binary_search(array5, target5))
