def solution(args :list):
    return ",".join(str(n) for n in args)

if __name__ == "__main__":
    print("Something")
    print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))