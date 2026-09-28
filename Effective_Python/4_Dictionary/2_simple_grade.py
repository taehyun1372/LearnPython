class SimpleGradebook:
    def __init__(self):
        self.__grades = {}

    def add_student(self, name):
        if not self.__grades.get(name):
            self.__grades[name] = []

    def report_grade(self, name, score):
        if not self.__grades.get(name):
            self.add_student(name)
        self.__grades[name].append(score)

    def average(self, name):
        grades = self.__grades[name]
        try:
            average = sum(grades) / len(grades)
        except Exception as ex:
            print("Cannot get average ", ex)
            average = None
        return average


if __name__ == "__main__":
    book = SimpleGradebook()
    book.report_grade("뉴튼", 90)
    book.add_student("뉴튼")
    book.report_grade("뉴튼", 90)
    book.report_grade("뉴튼", 85)
    book.report_grade("뉴튼", 70)
    book.report_grade("뉴튼", "감자")
    book.add_student("뉴튼")

    print("book average ", book.average("뉴튼"))
