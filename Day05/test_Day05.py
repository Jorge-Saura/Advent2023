#--- Day 8: Treetop Tree House ---

import unittest

import Day05.Day05 as challenges

class TestDay04(unittest.TestCase):

    def test_Cultivation(self):

        cultivation = challenges.Agriculture()

        cultivation._load_data("Day05\DataSimple.txt")
        self.assertEqual(cultivation.seeds[0],79)

        min_location = cultivation.get_min_location("Day05\DataSimple.txt")
        self.assertEqual(min_location, 35)
        

        min_location = cultivation.get_min_location("Day05\Data.txt")
        self.assertEqual(min_location, 836040384)
    

    def test__compose_range(self):

        cultivation = challenges.Agriculture()

        #Fuera por la izqd 
        composed = cultivation._compose_range((10,3),(0,20,10))
        self.assertEqual(composed[0], (10,3,'original'))

        composed = cultivation._compose_range((10,10),(0,20,10))
        self.assertEqual(composed[0], (10,10,'original'))

        # Fuera por la izqd dentro por la derecha
        composed = cultivation._compose_range((10,10),(0,15,20))
        self.assertEqual(composed[0], (10,5,'original'))
        self.assertEqual(composed[1], (0,5,'transformed'))

        composed = cultivation._compose_range((10,6),(0,15,20))
        self.assertEqual(composed[0], (10,5,'original'))
        self.assertEqual(composed[1], (0,1,'transformed'))

        # Dentro del rango
        composed = cultivation._compose_range((10,5),(0,5,25))
        self.assertEqual(composed[0], (5,5,'transformed'))

        composed = cultivation._compose_range((10,5),(0,10,5))
        self.assertEqual(composed[0], (0,5,'transformed'))

        composed = cultivation._compose_range((10,3),(0,10,5))
        self.assertEqual(composed[0], (0,3,'transformed'))

        composed = cultivation._compose_range((12,3),(0,10,5))
        self.assertEqual(composed[0], (2,3,'transformed'))

        composed = cultivation._compose_range((10,1),(0,10,5))
        self.assertEqual(composed[0], (0,1,'transformed'))

        composed = cultivation._compose_range((14,1),(0,10,5))
        self.assertEqual(composed[0], (4,1,'transformed'))

        #Dentro por la izqd fuera por la drch
        composed = cultivation._compose_range((15,10),(0,10,10))
        self.assertEqual(composed[0], (5,5,'transformed'))
        self.assertEqual(composed[1], (20,5,'original'))
        
        composed = cultivation._compose_range((19,2),(0,10,10))
        self.assertEqual(composed[0], (9,1,'transformed'))
        self.assertEqual(composed[1], (20,1,'original'))

        composed = cultivation._compose_range((57,13),(49,53,8))
        self.assertEqual(composed[0], (53,4,'transformed'))
        self.assertEqual(composed[1], (61,9,'original'))

        #Fuera por la drcha
        composed = cultivation._compose_range((25,5),(0,10,10))
        self.assertEqual(composed[0], (25,5,'original'))

        composed = cultivation._compose_range((20,5),(0,10,10))
        self.assertEqual(composed[0], (20,5,'original'))

        #Fuera por la izqd y drcha (es más grande que el rango a comprobar, lo contiene)
        composed = cultivation._compose_range((5,20),(0,10,10))
        self.assertEqual(composed[0], (5,5,'original'))
        self.assertEqual(composed[1], (0,10,'transformed'))
        self.assertEqual(composed[2], (20,5,'original'))

        composed = cultivation._compose_range((9,12),(0,10,10))
        self.assertEqual(composed[0], (9,1,'original'))
        self.assertEqual(composed[1], (0,10,'transformed'))
        self.assertEqual(composed[2], (20,1,'original'))





    def test_Cultivatio_2n(self):

        cultivation = challenges.Agriculture()

        min_location = cultivation.get_min_location_2("Day05\DataSimple.txt")
        self.assertEqual(min_location, 46)

        min_location = cultivation.get_min_location_2("Day05\Data.txt")
        self.assertEqual(min_location, 10834440)



if __name__ == "__main__":

    unittest.main()