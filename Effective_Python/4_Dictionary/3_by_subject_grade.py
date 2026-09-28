from collections import defaultdict

class BySubjectGradeBook:
    def __init__(self):
        self.__grades = {}

    def add_student(self, name):
        if name not in self.__grades:
            self.__grades[name] = defaultdict(list)

    def report_grade(self, name, subject, grade):
        if isinstance(grade, int) or isinstance(grade, float):
            raise Exception("Wrong type for the grade!")
        try:
            by_subject = self._grades[name]
        except KeyError:
            print(f"The name {name} does not exist!")
        else:
            grade_list = by_subject[subject]
            grade_list.append(grade)

    def average(self, name):
        try:
            by_subject = self.__grades[name]
        except KeyError:
            print(f"The name {name} does not exist!")
            return None
        else:
            total, count = 0, 0
            for grades in by_subject.values():
                total += sum(grades)
                count += len(grades)
            return total / count

if __name__ == "__main__":
    book = BySubjectGradeBook()
    book.add_student("뉴튼")
    book.report_grade("뉴튼", "수학", 20)
    book.report_grade("뉴튼")
    book.report_grade("뉴튼")
    book.report_grade("뉴튼")
