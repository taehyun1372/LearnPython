def tower_builder(n_floors):
    result = []
    temp_string = ""
    for i in range(n_floors):
        temp_string = ""
        temp_string += " " * (n_floors - (i + 1))
        temp_string += "*" * (2 * i + 1)
        result.append(temp_string)
    return result

if __name__ == "__main__":
    result = tower_builder(3)
    print(result)
    print("Hello")