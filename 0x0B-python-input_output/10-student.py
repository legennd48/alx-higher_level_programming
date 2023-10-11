#!/usr/bin/python3
'''
Module: 10. Student to JSON with filter
modifies 9-student.py by adding to_json method
'''


class Student:

    def __init__(self, first_name, last_name, age):
        '''instantiation of student class'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns dictionary description with simple data structure'''

        if(type(attrs) == list and all(type(element) == str
                                       for element in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
