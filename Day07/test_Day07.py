#--- Day 8: Treetop Tree House ---

import unittest

import Day07.Day07 as challenges

class TestDay07(unittest.TestCase):

    def test_load_data(self):

        cards = challenges.CamelCards()

        hands = cards._load_data("Day07\DataSimple.txt")
        self.assertEqual(len(hands),5)
        self.assertEqual(hands[0][0],'32T3K')
        self.assertEqual(hands[0][1],765)
 


if __name__ == "__main__":

    unittest.main()