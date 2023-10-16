#!/usr/bin/python3
'''
Module: 1. Base class
the “base” of all other classes in this project
'''
import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation"""

        if list_dictionaries is None:
            list_dictionaries = []

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file:"""
         name = cls.__name__ + ".json"

        with open(name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns Python obj of JSON string rep"""

        if json_string is None or len(json_string) == 0:
            json_string = "[]"

        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set: """
         if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return (dummy)

     @classmethod
    def load_from_file(cls):
        """Return a list of instanced from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        """
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Serializes and deserializes in CSV:
        '''
        file_name = cls.__name__ + ".csv"

        with open(file_name, 'w', newline='') as file_writer:
            csv_writer = csv.writer(file_writer)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    csv_writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                if cls.__name__ == "Square":
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])
