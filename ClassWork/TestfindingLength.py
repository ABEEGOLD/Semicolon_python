import unittest
from findingLength import numbers, length_list
from findingLength import numbers, sum_elements_at_even_position
from findingLength import numbers, sum_elements_at_odd_position
from findingLength import numbers, multiply_elements_at_third_position
from findingLength import numbers, calculate_the_average_of_all_elements_list


class MyTestLength(unittest.TestCase):
    def test_that_length_works(self):
       self.assertEqual(length_list([1, 2, 3, 4, 5, 6]), 6)

    def test_that_sum_elements_at_even_position_works(self):
       self.assertEqual(sum_elements_at_even_position([1, 2, 3, 4, 5, 6]), 12)

    def test_that_sum_elements_at_odd_position_exit(self):
        self.assertEqual(sum_elements_at_odd_position([1, 2, 3, 4, 5, 6]), 9)

    def test_that_multiply_elements_at_third_position_works(self):
        self.assertEqual(multiply_elements_at_third_position([1, 2, 3, 4, 5, 6]), 18)

    def test_that_it_Calculate_the_average_of_all_elements_list_works(self):
            self.assertEqual(calculate_the_average_of_all_elements_list([1, 2, 3, 4, 5, 6]), 3.5)