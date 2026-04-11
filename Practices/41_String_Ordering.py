from typing import List


def order_string_items(items : list, key: str):
    items = list(set(items))
    result = [item for item in items if key in item]
    result.sort()
    return result

if __name__ == "__main__":
    testee1 = ["ab", "ab", "abc", "bc", "bcd", "z", "12z"]
    print(order_string_items(testee1, "ab"))