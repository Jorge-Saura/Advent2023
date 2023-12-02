#--- Day 8: Treetop Tree House ---

import unittest

import Day01.Day01 as challenges

class TestDay01(unittest.TestCase):

    def test_Calibrator(self):

        calibrator = challenges.Calibrator()

        result = calibrator._read_data("Day01\DataSimple.txt")
        self.assertEqual(len(result),4)
        first_line_number = calibrator._process_line(result[0])
        second_line_number = calibrator._process_line(result[1])
        self.assertEqual(first_line_number,12)
        self.assertEqual(second_line_number,38)

        code = calibrator.get_calibrator_code("Day01\DataSimple.txt")
        self.assertEqual(code,142)
        code = calibrator.get_calibrator_code("Day01\Data.txt")
        self.assertEqual(code,55488)        

    def test_calibrator_2(self):

        calibrator = challenges.Calibrator()

        result = calibrator._read_data("Day01\DataSimple2.txt")
        first_digit = calibrator._get_first_digit(result[0])
        self.assertEqual(first_digit,2)

        first_digit = calibrator._get_first_digit(result[1])
        self.assertEqual(first_digit,8)

        
        num = calibrator._process_line(result[0])
        self.assertEqual(num,29)

        num = calibrator._process_line(result[1])
        self.assertEqual(num,83)

        code = calibrator.get_calibrator_code("Day01\DataSimple2.txt")
        self.assertEqual(code,281)
        code = calibrator.get_calibrator_code("Day01\Data.txt")
        self.assertEqual(code,55614)   


if __name__ == "__main__":

    unittest.main()