class Student:
    """ A class to handle student problem   
    Attributes:
    batch_size
    """
    def __init__(self):
        pass

def bad_reference(a):
    """
    This is to demonstrate a runtime error

    :a: input to add to the result
    """
    # print(my_var)
    my_var = 13 + a
    return my_var

if __name__ == "__main__":
    print("Something")
    secret = {"key1": "value1", "key2": "value2"}
    bad_reference(2)
