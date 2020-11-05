import unittest
import math
from geometry import Circle
from geometry import Rectangle


class MyTestCase(unittest.TestCase):
    def test_create_circle(self):
        circ = Circle(5.2)
        circ_string = str(circ)
        self.assertGreater(circ_string.find("5.2"), False)

    def test_create_circle_neg_radius(self):
        circ = Circle(-3.7)
        circ_string = str(circ)
        self.assertGreater(circ_string.find("3.7"), -1)

    def test_area_zero_radius(self):
        circ = Circle(8)
        area = circ.area
        self.assertEqual(0, area)
    def test_area(self):
        circ = Circle(1)
    def test_circumference(self):
        circ = Circle(1)
        self.assertEqual(math.pi, circ.circumference())

class MyTestCase(unittest.TestCase):
    def test_create_circle(self):
        rectangle = Rectangle(5.2, 5.2)
        rectangle_string = str(rectangle)
        self.assertGreater(rectangle.find("5.2"), False)

    def test_create_circle_neg_radius(self):
        rectangle = Rectangle(-3.7, -3.7)
        rectangle_string = str(rectangle)
        self.assertGreater(rectangle_string.find("3.7"), -1)

    def test_area_zero_radius(self):
        rectangle = Rectangle(0, 0)
        area = rectangle.area
        self.assertEqual(0, area)
    def test_area(self):
        rectangle = Rectangle(1, 1)
    def test_circumference(self):
        rectangle = Rectangle(1, 1)
        self.assertEqual(rectangle, Rectangle.perimeter())
