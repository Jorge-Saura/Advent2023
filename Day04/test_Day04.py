#--- Day 8: Treetop Tree House ---

import unittest

import Day04.Day04 as challenges

class TestDay04(unittest.TestCase):

    def test_GearRatios(self):

        cards = challenges.Scratchcards()

        result = cards._read_data("Day04\DataSimple.txt")
        self.assertEqual(len(result),6)

        numbers = cards._get_numbers_in_line('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
        self.assertEqual(numbers[41],1)

        winnig_points = cards.get_cards_points("Day04\DataSimple.txt")
        self.assertEqual(winnig_points, 13)

        winnig_points = cards.get_cards_points("Day04\Data.txt")
        self.assertEqual(winnig_points, 23028)




if __name__ == "__main__":

    unittest.main()