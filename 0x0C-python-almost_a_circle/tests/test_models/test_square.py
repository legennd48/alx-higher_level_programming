#!/usr/bin/python3
'''
unit trst for square.py
'''
import unittest
from models.square import Square
import io
import sys
from models.base import Base


class TestSquare(unittest.TestCase):
    def test_init(self):
        """Test that the Square class can be initialized with valid arguments."""
        square = Square(10, 2, 3, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_size_getter_and_setter(self):
        """Test that the size getter and setter work as expected."""
        square = Square(10)
        self.assertEqual(square.size, 10)

        square.size = 20
        self.assertEqual(square.size, 20)

        with self.assertRaises(TypeError):
            square.size = "hello"

        with self.assertRaises(ValueError):
            square.size = -1

    def test_area(self):
        """Test that the area method calculates the area of the square correctly."""
        square = Square(10)
        self.assertEqual(square.area(), 100)

    def test_display(self):
        """Test that the display method prints the square correctly."""
        pass

    def test_str(self):
        """Test that the str method returns the correct string representation of the square."""
        square = Square(10, 2, 3, 1)
        output = "[Square] (1) 2/3 - 10"

        self.assertEqual(str(square), output)

    def test_update(self):
        """Test that the update method updates the attributes of the square correctly."""
        square = Square(10)

        square.update(id=2, size=20, x=3, y=4)

        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_to_dictionary(self):
        """Test that the to_dictionary method returns a correct dictionary representation of the square."""
        square = Square(10, 2, 3, 1)
        expected_dict = {"id": 1, "size": 10, "x": 2, "y": 3}

        self.assertEqual(square.to_dictionary(), expected_dict)
