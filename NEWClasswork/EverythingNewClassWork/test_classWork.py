import unittest
from EverythingNewClassWork.classWork import access_the_third_element
from EverythingNewClassWork.classWork import change_the_last_item_in_the_color

class TestClassWork(unittest.TestCase):
    def test_to_access_the_third_element_works(self):
       self.assertEqual(access_the_third_element([10,20,30,40,50]), 30)

    def test_change_the_last_item_in_the_color_to_works(self):
        self.assertEqual(change_the_last_item_in_the_color( ['red','green','blue']),   "yellow")
