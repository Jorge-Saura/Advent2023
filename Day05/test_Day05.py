#--- Day 8: Treetop Tree House ---

import unittest

import Day05.Day05 as challenges

class TestDay04(unittest.TestCase):

    def test_Scratchcards(self):

        cultivation = challenges.Agriculture()

        cultivation._load_data("Day05\DataSimple.txt")
        self.assertEqual(cultivation.seeds[0],79)

        min_location = cultivation.get_min_location("Day05\DataSimple.txt")
        self.assertEqual(min_location, 35)
        

        min_location = cultivation.get_min_location("Day05\Data.txt")
        self.assertEqual(min_location, 35)





if __name__ == "__main__":

    unittest.main()