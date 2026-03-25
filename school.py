from collections.abc import Iterable, Iterator


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


class StudentIteratorMatter1(Iterator):

    def __init__(self, students: list):
        self.__students = sorted(students, key=lambda s: s.matter1, reverse=True)
        self.__index = 0

    def __next__(self) -> Student:
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class StudentIteratorMatter2(Iterator):

    def __init__(self, students: list):
        self.__students = sorted(students, key=lambda s: s.matter2, reverse=True)
        self.__index = 0

    def __next__(self) -> Student:
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class StudentIteratorMatter3(Iterator):

    def __init__(self, students: list):
        self.__students = sorted(students, key=lambda s: s.matter3, reverse=True)
        self.__index = 0

    def __next__(self) -> Student:
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class SchoolClass(Iterable):

    def __init__(self):
        self._students = []

    def add_student(self, student: Student):
        self._students.append(student)

    def __iter__(self) -> StudentIteratorMatter1:
        return StudentIteratorMatter1(self._students)

    def iter_matter_2(self) -> StudentIteratorMatter2:
        return StudentIteratorMatter2(self._students)

    def iter_matter_3(self) -> StudentIteratorMatter3:
        return StudentIteratorMatter3(self._students)


if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print('\n Iterator Matière 1 ')
    for student in school_class:
        print(student)

    print('\n Iterator Matière 2 ')
    for student in school_class.iter_matter_2():
        print(student)

    print('\n Iterator Matière 3 ')
    for student in school_class.iter_matter_3():
        print(student)