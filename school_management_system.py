from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    @abstractmethod
    def display_info(self):
        pass

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__course = course

    def get_student_id(self):
        return self.__student_id

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def display_info(self):
        print("\n----- STUDENT -----")
        print(f"Name      : {self.get_name()}")
        print(f"Age       : {self.get_age()}")
        print(f"ID        : {self.__student_id}")
        print(f"Course    : {self.__course}")

class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__subject = subject

    def get_employee_id(self):
        return self.__employee_id

    def get_subject(self):
        return self.__subject