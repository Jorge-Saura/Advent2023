#--- Day 8: Treetop Tree House ---

import unittest

import Day09.Day09 as challenges
from itertools import permutations


class TestDay09(unittest.TestCase):

    def test_load_data(self):

        mirage = challenges.Mirage()
        data = mirage._load_data("Day09\DataSimple.txt")
        self.assertEqual(len(data),3)
        self.assertEqual(data[0][0],0)
        self.assertEqual(data[2][5],45)
    
    def test_get_difference(self):

        mirage = challenges.Mirage()
        data = mirage._get_differences([1,1])
        self.assertEqual(len(data),1)
        self.assertEqual(data[0],0)
        data = mirage._get_differences([3,6,9])
        self.assertEqual(len(data),2)
        self.assertEqual(data[0],3)
        self.assertEqual(data[1],3)


        

    def test_get_next_number(self):

        mirage = challenges.Mirage()
        data = mirage._get_next_number([3,15],[0,3])
        self.assertEqual(data,18)   

        data = mirage._get_next_number([1,6,21],[0,1,6])
        self.assertEqual(data,28)        

        data = mirage._get_next_number([2,6,15,45],[0,2,6,15])
        self.assertEqual(data,68)                

    def test_get_next_numbers(self):

        mirage = challenges.Mirage()
        data = mirage.get_next_numbers("Day09\DataSimple.txt")
        self.assertEqual(data,114)        

        mirage = challenges.Mirage()
        data = mirage.get_next_numbers("Day09\Data.txt")
        self.assertEqual(data,114)      

    

if __name__ == "__main__":

    unittest.main()