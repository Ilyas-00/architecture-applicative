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

    def rank_matter_1(self):
        print('\n--- Classement Matière 1 ---')
        for s in sorted(self._students, key=lambda s: s.matter1, reverse=True):
            print(s)

    def rank_matter_2(self):
        print('\n--- Classement Matière 2 ---')
        for s in sorted(self._students, key=lambda s: s.matter2, reverse=True):
            print(s)

    def rank_matter_3(self):
        print('\n--- Classement Matière 3 ---')
        for s in sorted(self._students, key=lambda s: s.matter3, reverse=True):
            print(s)


if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()