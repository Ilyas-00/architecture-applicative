from collections.abc import Iterable, Iterator
from abc import ABCMeta


class SingletonMeta(ABCMeta):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


def add_matter4(cls):
    original_init = cls.__init__

    def new_init(self, name: str, matter1: float, matter2: float,
                 matter3: float, matter4: float = 0):
        original_init(self, name, matter1, matter2, matter3)
        self.matter4 = matter4

    def new_average(self) -> float:
        return (self.matter1 + self.matter2 + self.matter3 + self.matter4) / 4

    def new_str(self) -> str:
        return (f'{self.name} | M1:{self.matter1} M2:{self.matter2} '
                f'M3:{self.matter3} M4:{self.matter4} '
                f'| avg:{self.average():.2f}')

    cls.__init__ = new_init
    cls.average = new_average
    cls.__str__ = new_str
    return cls


def add_iter_matter4(cls):

    class StudentIteratorMatter4(Iterator):
        def __init__(self, students: list):
            self.__students = sorted(students, key=lambda s: s.matter4, reverse=True)
            self.__index = 0

        def __next__(self):
            if self.__index >= len(self.__students):
                raise StopIteration
            student = self.__students[self.__index]
            self.__index += 1
            return student

    def iter_matter_4(self):
        return StudentIteratorMatter4(self._students)

    cls.iter_matter_4 = iter_matter_4
    return cls


@add_matter4
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
    def __init__(self, students):
        self.__students = sorted(students, key=lambda s: s.matter1, reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        s = self.__students[self.__index]
        self.__index += 1
        return s


class StudentIteratorMatter2(Iterator):
    def __init__(self, students):
        self.__students = sorted(students, key=lambda s: s.matter2, reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        s = self.__students[self.__index]
        self.__index += 1
        return s


class StudentIteratorMatter3(Iterator):
    def __init__(self, students):
        self.__students = sorted(students, key=lambda s: s.matter3, reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        s = self.__students[self.__index]
        self.__index += 1
        return s


@add_iter_matter4
class SchoolClass(Iterable, metaclass=SingletonMeta):

    def __init__(self):
        self._students = []

    def add_student(self, student: Student):
        self._students.append(student)

    def __iter__(self):
        return StudentIteratorMatter1(self._students)

    def iter_matter_2(self):
        return StudentIteratorMatter2(self._students)

    def iter_matter_3(self):
        return StudentIteratorMatter3(self._students)


if __name__ == '__main__':
    # Test Singleton
    school_class = SchoolClass()
    school_class_copy = SchoolClass()
    assert school_class is school_class_copy
    print('Singleton OK : même instance')

    school_class.add_student(Student('J', 10, 12, 13, 15))
    school_class.add_student(Student('A', 8, 2, 17, 11))
    school_class.add_student(Student('V', 9, 14, 14, 18))

    print('\n Iterator Matière 1 ')
    for student in school_class:
        print(student)

    print('\n Iterator Matière 2 ')
    for student in school_class.iter_matter_2():
        print(student)

    print('\n Iterator Matière 3 ')
    for student in school_class.iter_matter_3():
        print(student)

    print('\n Iterator Matière 4 ')
    for student in school_class.iter_matter_4():
        print(student)