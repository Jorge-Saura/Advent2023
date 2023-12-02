#--- Day 8: Treetop Tree House ---

import unittest

import Day02.Day02 as challenges

class TestDay02(unittest.TestCase):

    def test_CubeGame(self):

        CubeGame = challenges.CubeGame()

        result = CubeGame._read_data("Day02\DataSimple.txt")
        self.assertEqual(len(result),5)

        dictionary = CubeGame._process_line(result[0])
        self.assertEqual(dictionary['red'],4)
        self.assertEqual(dictionary['green'],2)
        self.assertEqual(dictionary['blue'],6)

        good_games = CubeGame.get_good_games("Day02\DataSimple.txt")
        self.assertEqual(good_games,8)

        good_games = CubeGame.get_good_games("Day02\Data.txt")
        self.assertEqual(good_games,2685)

    def test_CubeGame_2(self):
        CubeGame = challenges.CubeGame()

        power_games = CubeGame.get_power_games("Day02\DataSimple.txt")
        self.assertEqual(power_games,2286)

        power_games = CubeGame.get_power_games("Day02\Data.txt")
        self.assertEqual(power_games,83707)


if __name__ == "__main__":

    unittest.main()