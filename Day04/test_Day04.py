#--- Day 8: Treetop Tree House ---

import unittest

import Day04.Day04 as challenges

class TestDay04(unittest.TestCase):

    def test_Scratchcards(self):

        cards = challenges.Scratchcards()

        result = cards._read_data("Day04\DataSimple.txt")
        self.assertEqual(len(result),6)

        numbers = cards._get_numbers_in_line('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
        self.assertEqual(numbers[41],1)

        winnig_points = cards.get_cards_points("Day04\DataSimple.txt")
        self.assertEqual(winnig_points, 13)

        winnig_points = cards.get_cards_points("Day04\Data.txt")
        self.assertEqual(winnig_points, 23028)


    def test_Scratchcards_2(self):

        cards = challenges.Scratchcards()

        d = {0:2,1:1,5:7}
        d = cards._add_copy_cards(d,starting_card=1,next_cards_win=5,num_copies_starting_card=1)
        self.assertEqual(d[1], 2)
        self.assertEqual(d[5], 8)

        d = {0:2,1:1,5:7}
        d = cards._add_copy_cards(d,starting_card=1,next_cards_win=5,num_copies_starting_card=2)
        self.assertEqual(d[1], 3)
        self.assertEqual(d[5], 9)


        winnig_points = cards.get_cards_points_2("Day04\DataSimple.txt")
        self.assertEqual(winnig_points, 30)

        winnig_points = cards.get_cards_points_2("Day04\Data.txt")
        self.assertEqual(winnig_points, 9236992)
        

if __name__ == "__main__":

    unittest.main()