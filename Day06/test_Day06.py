#--- Day 8: Treetop Tree House ---

import unittest

import Day06.Day06 as challenges

class TestDay06(unittest.TestCase):

    def test_load_data(self):

        race = challenges.BoatRace()

        d = race._load_data("Day06\DataSimple.txt")
        self.assertEqual(d[7],9)
        self.assertEqual(d[15],40)
        self.assertEqual(d[30],200)
        self.assertEqual(len(d.keys()),3)

    def test_get_times_higher_distances(self):

        race = challenges.BoatRace()

        d = race._get_times_higher_distances(7,9)
        self.assertEqual(len(d),4)
        self.assertEqual(d[0],2)
        self.assertEqual(d[1],3)
        self.assertEqual(d[2],4)
        self.assertEqual(d[3],5)


        d = race._get_times_higher_distances(15,40)
        self.assertEqual(len(d),8)
        # self.assertEqual(d[0],2)
        # self.assertEqual(d[1],3)
        # self.assertEqual(d[2],4)
        # self.assertEqual(d[3],5)

    def test_get_good_times(self):

        race = challenges.BoatRace()

        d = race.get_good_times("Day06\DataSimple.txt")
        self.assertEqual(d,288)

        d = race.get_good_times("Day06\Data.txt")
        self.assertEqual(d,588588)

    def test_get_times_big_number_(self):

        race = challenges.BoatRace()

        d = race._get_times_higher_distances(44826981,202107611381458)
        self.assertEqual(len(d),34655848)


if __name__ == "__main__":

    unittest.main()