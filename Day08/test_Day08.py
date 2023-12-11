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
        self.assertEqual(steps,19637)

    def test_nodes_ending_with(self):

        navigator = challenges.NetworkNavigator()
        data = navigator._get_nodes_ending_with_char(['AB','BC','ZZ','EE','AZ'], 'Z')
        self.assertEqual(data,['ZZ','AZ'])    

    def test_multiple_starts(self):

        navigator = challenges.NetworkNavigator()
        data = navigator.get_number_of_steps_multiple_starts("Day08\DataSimple3.txt")
        self.assertEqual(data,6)

        data = navigator.get_number_of_steps_multiple_starts("Day08\Data.txt")
        self.assertEqual(data,8811050362409)

if __name__ == "__main__":

    unittest.main()