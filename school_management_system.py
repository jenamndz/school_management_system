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