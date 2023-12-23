#--- Day 8: Treetop Tree House ---

import unittest

import Day11.Day11 as challenges

class TestDay11(unittest.TestCase):

    def test_load_data(self):

        cosmos = challenges.CosmicExpansion()

        universe = cosmos._load_data("Day11\DataSimple.txt")
        self.assertEqual(len(universe),10)


    def test_empty_lines(self):
        cosmos = challenges.CosmicExpansion()

        universe = cosmos._load_data("Day11\DataSimple.txt")
        empty_hor = cosmos._get_horizontal_empty_lines(universe)
        self.assertEqual(len(empty_hor),2)
        self.assertEqual(empty_hor,[3,7])


        empty_ver = cosmos._get_vertical_empty_lines(universe)
        self.assertEqual(len(empty_ver),3)
        self.assertEqual(empty_ver,[2,5,8])
    
    def test_add_lines(self):
        cosmos = challenges.CosmicExpansion()

        universe = cosmos._load_data("Day11\DataSimple.txt")
        expanded_universe = cosmos._add_horizontal_line(universe, 0)
        self.assertEqual(len(expanded_universe),11)
        self.assertEqual(expanded_universe[0],'..........')

        universe = cosmos._load_data("Day11\DataSimple.txt")
        expanded_universe = cosmos._add_horizontal_line(universe, 5)
        self.assertEqual(len(expanded_universe),11)
        self.assertEqual(expanded_universe[5],'..........')

        universe = cosmos._load_data("Day11\DataSimple.txt")
        expanded_universe = cosmos._add_vertical_line(universe, 0)
        self.assertEqual(len(expanded_universe[0]),11)
        self.assertEqual(expanded_universe[0],'....#......')

    def test_get_galaxies(self):

        cosmos = challenges.CosmicExpansion()

        universe = cosmos._load_data("Day11\DataSimple.txt")
        galaxies = cosmos._get_galaxies(universe)

        self.assertEqual(len(galaxies),9)
        self.assertEqual(galaxies[0],(3,0))

    def test_get_shortest_paths(self):

        cosmos = challenges.CosmicExpansion()

        num = cosmos.get_shortest_paths("Day11\DataSimple.txt")
        self.assertEqual(num,374)

        num = cosmos.get_shortest_paths("Day11\Data.txt")
        self.assertEqual(num,10173804)


if __name__ == "__main__":

    unittest.main()