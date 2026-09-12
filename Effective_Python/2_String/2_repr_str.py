my_value = "foo bar"
print(str(my_value))
print("%s" % my_value)
print(f"{my_value}")
print(format(my_value))
print(my_value.__format__("s"))
print(my_value.__str__())

class Student:

    def __str__(self):
        return "this is student str"

    def __repr__(self):
        return "This is student repr"

roy = Student()
print(roy)

my_test1 = "hello" "beautiful" "world"
my_test2 = "hello" + "beautiful" + "world"
assert my_test1 == my_test2

