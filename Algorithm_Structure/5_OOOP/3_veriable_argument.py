def add(*args):
    total = 0
    for i in args:
        total += i
    return total

def print_items(*args):
    for i, item in enumerate(args):
        print(f"{i}th item : {item}")

def print_options(**kwargs):
    for k, v in kwargs.items():
        print(f"key : {k}, value : {v}")

def print_details(*args, **kwargs):
    for i, item in enumerate(args):
        print(f"{i}th item : {item}")

    for k, v in kwargs.items():
        print(f"key : {k}, value : {v}")

if __name__ == "__main__":
    print(add(10, 20))
    list1 = ["banana", "tomato", "key"]
    print_items(*list1)
    print_options(telnet = "good", interstela = "amazaing")
    print_details(1, 2, "abc", min=3, limit=5)
