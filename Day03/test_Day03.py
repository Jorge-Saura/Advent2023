#--- Day 8: Treetop Tree House ---

import unittest

import Day03.Day03 as challenges

class TestDay03(unittest.TestCase):

    def test_GearRatios(self):

        engine = challenges.GearRatios()

        # result = engine._read_data("Day03\DataSimple.txt")
        # self.assertEqual(len(result),10)

        numbers = engine._get_numbers_in_line('467..114..')
        self.assertEqual(numbers[0][0],467)
        self.assertEqual(numbers[0][1],0)
        self.assertEqual(numbers[0][2],2)
        self.assertEqual(numbers[1][0],114)
        self.assertEqual(numbers[1][1],5)
        self.assertEqual(numbers[1][2],7)


        numbers = engine._get_numbers_in_line('......1')
        self.assertEqual(numbers[0][0],1)


        ratios = engine.get_gear_ratios("Day03\DataSimple.txt")
        self.assertEqual(ratios, 4362)

        ratios = engine.get_gear_ratios("Day03\Data.txt")
        self.assertEqual(ratios, 4361)

    # def test_pruebas(self):

    #     self.assertEqual("1234"[0:6],"1234")




if __name__ == "__main__":

    unittest.main()