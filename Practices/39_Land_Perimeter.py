from win32com.client.util import Enumerator


def land_perimeter(arr):
    totalCount = 0
    currentColumnIndex = []
    previousColumnIndex = []
    horizontal_overlap = 0
    vertical_overlap = 0
    for r, row in enumerate(arr):
        for c, item in enumerate(row):
            if item == 'X':
                totalCount += 1
                if c >= 1 and row[c-1] == "X":
                    horizontal_overlap += 1

                if r >= 1 and arr[r-1][c] == "X":
                    vertical_overlap += 1

    print(totalCount, horizontal_overlap, vertical_overlap)

    return "Total land perimeter: " + str(totalCount * 4 - horizontal_overlap * 2 - vertical_overlap * 2)

if __name__ == "__main__":
    print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))
    print(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]))
    print(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]))
