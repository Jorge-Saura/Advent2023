#--- Day 8: Treetop Tree House ---

import unittest

import Day08.Day08 as challenges
from itertools import permutations


class TestDay08(unittest.TestCase):

    def test_load_data(self):

        navigator = challenges.NetworkNavigator()
        data = navigator._load_data("Day08\DataSimple.txt")
        self.assertEqual(len(data),2)

        steps = navigator.get_number_of_steps("Day08\DataSimple.txt")
        self.assertEqual(steps,2)

        steps = navigator.get_number_of_steps("Day08\DataSimple2.txt")
        self.assertEqual(steps,6)

        steps = navigator.get_number_of_steps("Day08\Data.txt")
        self.assertEqual(steps,6)
    

if __name__ == "__main__":

    unittest.main()