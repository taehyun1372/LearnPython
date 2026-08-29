class GFGClass:
    gfg_count = 0

    def __init__(self):
        GFGClass.gfg_count+=1

    @classmethod
    def print_instance_count(cls):
        print(f"{cls.gfg_count}th gfg created")

class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def create_instance_from_text(cls, text: str):
        args= text.split(',')
        return Student(name=args[0], age=args[1])

    @property
    def name(self):
        print("name getter called")
        return self._name

    @name.setter
    def name(self, name):
        print("name setter called")
        self._name = name

from abc import abstractmethod, ABC
class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self) -> int:
        pass

class Square(Shape):
    def __init__(self):
        print("a square is created")

    def area(self, length):
        return str(length * length)
    

if __name__ == "__main__":
    gfg1 = GFGClass()
    gfg2 = GFGClass()
    GFGClass.print_instance_count()

    student1 = Student.create_instance_from_text("Roy,35")
    student1.name = "Taehyun"
    print(student1.name)

    square1 = Square()
    print(square1.area(3))
