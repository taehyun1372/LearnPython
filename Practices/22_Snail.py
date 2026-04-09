
def snail(snail_map):
    col = [row[2] for row in snail_map]
    return col

def get_line(snail_map, start_row, start_col):
    pass

if __name__ == "__main__":

    array1 = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    result1 = snail(array1)

    print(result1)
    print("Hello World")
