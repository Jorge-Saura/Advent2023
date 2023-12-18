#--- Day 8: Treetop Tree House ---

import unittest

import Day10.Day10 as challenges
from itertools import permutations


class TestDay10(unittest.TestCase):

    def test_load_data(self):

        maze = challenges.Maze()
        data = maze._load_data("Day10\DataSimple.txt")
        self.assertEqual(len(data),2)
        self.assertEqual(data[0],(1,1))
        self.assertEqual(data[1][0][1],'.')

    def test_get_connectors(self):

        pipeMaze = challenges.Maze()
        start, maze = pipeMaze._load_data("Day10\DataSimple.txt")
        connectors = pipeMaze._get_connectors((3,1),maze)
        self.assertEqual(connectors[0],(2,1))
        self.assertEqual(connectors[1],(3,2))

        connectors = pipeMaze._get_connectors((3,2),maze)
        self.assertEqual(connectors[0],(3,1))
        self.assertEqual(connectors[1],(3,3))

        connectors = pipeMaze._get_connectors((3,3),maze)
        self.assertEqual(connectors[0],(3,2))
        self.assertEqual(connectors[1],(2,3))

        connectors = pipeMaze._get_connectors((2,3),maze)
        self.assertEqual(connectors[0],(1,3))
        self.assertEqual(connectors[1],(3,3))

        connectors = pipeMaze._get_connectors((1,3),maze)
        self.assertEqual(connectors[0],(1,2))
        self.assertEqual(connectors[1],(2,3))

        connectors = pipeMaze._get_connectors((0,0),['F'])
        self.assertEqual(connectors[0],(1,0))
        self.assertEqual(connectors[1],(0,1))

        connectors = pipeMaze._get_connectors((1,1),maze)
        self.assertEqual(connectors[0],(2,1))
        self.assertEqual(connectors[1],(1,2))

        start, maze = pipeMaze._load_data("Day10\DataSimple2.txt")
        connectors = pipeMaze._get_connectors((0,2),maze)
        self.assertEqual(connectors[0],(1,2))
        self.assertEqual(connectors[1],(0,3))


    

    def test_get_surounding_points(self):

        pipeMaze = challenges.Maze()
        
        points = pipeMaze._get_surrounding_points((0,0),4,4)
        self.assertEqual(len(points),3)

        points = pipeMaze._get_surrounding_points((1,1),4,4)
        self.assertEqual(len(points),8)

        points = pipeMaze._get_surrounding_points((1,0),4,4)
        self.assertEqual(len(points),5)

        points = pipeMaze._get_surrounding_points((3,3),4,4)
        self.assertEqual(len(points),3)


    def test_get_max_distance(self):

        pipeMaze = challenges.Maze()
        max_distance = pipeMaze.get_max_distance("Day10\DataSimple.txt")
        self.assertEqual(max_distance,4)

        max_distance = pipeMaze.get_max_distance("Day10\DataSimple1.txt")
        self.assertEqual(max_distance,4)

        max_distance = pipeMaze.get_max_distance("Day10\DataSimple2.txt")
        self.assertEqual(max_distance,8)

        max_distance = pipeMaze.get_max_distance("Day10\Data.txt")
        self.assertEqual(max_distance,6768)


if __name__ == "__main__":

    unittest.main()