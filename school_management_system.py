from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age