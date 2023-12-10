#--- Day 8: Treetop Tree House ---

import unittest

import Day07.Day07 as challenges
from itertools import permutations


class TestDay07(unittest.TestCase):

    def test_load_data(self):

        cards = challenges.CamelCards()

        hands = cards._load_data("Day07\DataSimple.txt")
        self.assertEqual(len(hands),5)
        self.assertEqual(hands[0][0],'ONVOY')
        self.assertEqual(hands[0][1],765)
        self.assertEqual(hands[1][0],'VQQWQ')
        self.assertEqual(hands[1][1],684)

    def test_get_hand_type(self):

        cards = challenges.CamelCards()

        hand = cards._get_hand_type('KKKKK')
        self.assertEqual(hand,'five')

        p = {"".join(p) for p in permutations('KK4KK')}

        for value in p:
            hand = cards._get_hand_type(value)
            self.assertEqual(hand,'four')
 
        p = {"".join(p) for p in permutations('KKK11')}

        for value in p:
            hand = cards._get_hand_type(value)
            self.assertEqual(hand,'full')

        p = {"".join(p) for p in permutations('KKK31')}

        for value in p:
            hand = cards._get_hand_type(value)
            self.assertEqual(hand,'three')

        p = {"".join(p) for p in permutations('KK233')}

        for value in p:
            hand = cards._get_hand_type(value)
            self.assertEqual(hand,'two')

        p = {"".join(p) for p in permutations('KK234')}

        for value in p:
            hand = cards._get_hand_type(value)
            self.assertEqual(hand,'one')

        p = {"".join(p) for p in permutations('K2345')}

        for value in p:
            hand = cards._get_hand_type(value)
            self.assertEqual(hand,'high')

    def test_get_total_winnings(self):

        cards = challenges.CamelCards()

        total = cards.get_total_winnings("Day07\DataSimple.txt")
        self.assertEqual(total,6440)

        # 209380301 too low
        total = cards.get_total_winnings("Day07\Data.txt")
        self.assertEqual(total,249638405)

    def test_get_hand_type_with_joker(self):

        cards = challenges.CamelCards()

        hand = cards._get_hand_type_with_joker('AAAAA')
        self.assertEqual(hand,'five')

        hand = cards._get_hand_type_with_joker('ZZZZZ')
        self.assertEqual(hand,'five')

        hand = cards._get_hand_type_with_joker('ZZZZA')
        self.assertEqual(hand,'five')

        hand = cards._get_hand_type_with_joker('ZZAVV')
        self.assertEqual(hand,'full')

        hand = cards._get_hand_type_with_joker('ZZAPO')
        self.assertEqual(hand,'three')

        hand = cards._get_hand_type_with_joker('ZAAPO')
        self.assertEqual(hand,'three')

        hand = cards._get_hand_type_with_joker('ZARPO')
        self.assertEqual(hand,'one')

    def test_get_total_winnings_with_joker(self):

        cards = challenges.CamelCards()

        total = cards.get_total_winnings_with_joker("Day07\DataSimple.txt")
        self.assertEqual(total,5905)

        total = cards.get_total_winnings_with_joker("Day07\Data.txt")
        self.assertEqual(total,249776650)

if __name__ == "__main__":

    unittest.main()