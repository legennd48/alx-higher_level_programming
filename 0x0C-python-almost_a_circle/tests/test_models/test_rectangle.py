#!/usr/bin/python3
''' tests for rectangle.py'''
import unittest
from models.rectangle import Rectangle
import io
import sys
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_init(self):
        """Test that the Rectangle class can be initialized with valid arguments."""
        rectangle = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_width_getter_and_setter(self):
        """Test that the width getter and setter work as expected."""
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.width, 10)

        rectangle.width = 20
        self.assertEqual(rectangle.width, 20)

        with self.assertRaises(TypeError):
            rectangle.width = "hello"

        with self.assertRaises(ValueError):
            rectangle.width = -1

    def test_height_getter_and_setter(self):
        """Test that the height getter and setter work as expected."""
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.height, 5)

        rectangle.height = 10
        self.assertEqual(rectangle.height, 10)

        with self.assertRaises(TypeError):
            rectangle.height = "hello"

        with self.assertRaises(ValueError):
            rectangle.height = -1

    def test_x_getter_and_setter(self):
        """Test that the x getter and setter work as expected."""
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.x, 0)

        rectangle.x = 2
        self.assertEqual(rectangle.x, 2)

        with self.assertRaises(TypeError):
            rectangle.x = "hello"

        with self.assertRaises(ValueError):
            rectangle.x = -1

    def test_y_getter_and_setter(self):
        """Test that the y getter and setter work as expected."""
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.y, 0)

        rectangle.y = 2
        self.assertEqual(rectangle.y, 2)

        with self.assertRaises(TypeError):
            rectangle.y = "hello"

        with self.assertRaises(ValueError):
            rectangle.y = -1

    def test_area(self):
        """Test that the area method calculates the area of the rectangle correctly."""
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.area(), 50)

    def test_display(self):
        """Test that the display method prints the rectangle correctly."""
        rectangle = Rectangle(10, 5)
        output = """

        #####
        #####
        #####"""

        self.assertEqual(rectangle.display(), output)

    def test_str(self):
        """Test that the str method returns the correct string representation of the rectangle."""
        rectangle = Rectangle(10, 5, 2, 3, 1)
        output = "[Rectangle] (1) 2/3 - 10/5"

        self.assertEqual(str(rectangle), output)

    def test_update(self):
        """Test that the update method updates the attributes of the rectangle correctly."""
        rectangle = Rectangle(10, 5)

        rectangle.update(id=2, width=20, height=10, x=3, y=4)

        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 20)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

        rectangle.update(width="hello")

        with self.assertRaises(TypeError):
            rectangle.width = "hello"

        rectangle.update(width=-1)

        with self.assertRaises(ValueError):
            rectangle.width = -1
