class Student:

    def __init__(self, name: str, matter1: float, matter2: float, matter3: float):
        self.name = name
        self.matter1 = matter1
        self.matter2 = matter2
        self.matter3 = matter3

    def average(self) -> float:
        return (self.matter1 + self.matter2 + self.matter3) / 3

    def __str__(self):
        return (f'{self.name} | M1:{self.matter1} M2:{self.matter2} M3:{self.matter3} '
                f'| avg:{self.average():.2f}')


class SchoolClass:

    def __init__(self):
        self._students = []

    def add_student(self, student: Student):
        self._students.append(student)


if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    for s in school_class._students:
        print(s)