#!/usr/bin/python3
'''
Module: 1. Base class
the “base” of all other classes in this project
'''


class Base:
    ''' Base class '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' initialisation of class object
        Args:
            id (int): id of object
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
