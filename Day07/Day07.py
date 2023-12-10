from functools import reduce
from collections import Counter
import re

class CamelCards:

    def _load_data(self, path:str)-> list:
        
        hands = list()
        with open(path, "r") as file:
            # Reading from a file
            for line in file:
                cards, bid = line.replace('\n','').split(' ')

                tranlated_cards = cards.translate(str.maketrans({'A': 'Z'
                                                       , 'K': 'Y'
                                                       , 'Q': 'X'
                                                       , 'J': 'W'
                                                       , 'T': 'V'
                                                       , '9': 'U'
                                                       , '8': 'T'
                                                       , '7': 'S'
                                                       , '6': 'R'
                                                       , '5': 'Q'
                                                       , '4': 'P'
                                                       , '3': 'O'
                                                       , '2': 'N'}))
                hands.append((tranlated_cards,int(bid), cards))

  
        return hands
    
    def _get_hand_type(self, cards:str) -> str:

        # types are: five, four, full, three, two, one, high

        numbers = Counter(cards)
        numbers = sorted(numbers.items(),key=lambda item: item[1],reverse=True)
        if numbers[0][1] == 5:
            return 'five'
        if numbers[0][1] == 4:
            return 'four'
        if numbers[0][1] == 3 and numbers[1][1] == 2:
            return 'full'
        if numbers[0][1] == 3 and numbers[1][1] == 1:
            return 'three'
        if numbers[0][1] == 2 and numbers[1][1] == 2:
            return 'two'
        if numbers[0][1] == 2 and numbers[1][1] == 1:
            return 'one'
        if numbers[0][1] == 1:
            return 'high'

        return 'otro'
    
    def get_total_winnings(self, path:str)-> int:

        hands = self._load_data(path)
        total_winnings = 0
        sorted_bids = list()
        hand_types = dict()

        
        for cards,bid, original in hands:
            hand_type = self._get_hand_type(cards)
            current_list = hand_types.get(hand_type, list())
            current_list.append((cards,bid, original))
            hand_types[hand_type] = current_list
        

        
        bids = hand_types.get('high',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('one',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('two',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('three',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('full',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('four',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('five',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        
        for pos, bid in enumerate(sorted_bids,1):
            total_winnings +=  pos * bid[1]

        return total_winnings

    def _load_data_with_joker(self, path:str)-> list:
        
        hands = list()
        with open(path, "r") as file:
            # Reading from a file
            for line in file:
                cards, bid = line.replace('\n','').split(' ')

                tranlated_cards = cards.translate(str.maketrans({'A': 'Z'
                                                       , 'K': 'Y'
                                                       , 'Q': 'X'
                                                       , 'J': 'A'
                                                       , 'T': 'V'
                                                       , '9': 'U'
                                                       , '8': 'T'
                                                       , '7': 'S'
                                                       , '6': 'R'
                                                       , '5': 'Q'
                                                       , '4': 'P'
                                                       , '3': 'O'
                                                       , '2': 'N'}))
                hands.append((tranlated_cards,int(bid), cards))

  
        return hands

    def _get_hand_type_with_joker(self, cards:str) -> str:
        

        # types are: five, four, full, three, two, one, high

        numbers = Counter(cards)
        numbers = sorted(numbers.items(),key=lambda item: (item[1], item[0]),reverse=True)

        jokers = next((x[1] for x in numbers if x[0] == 'A'), 0)
        if jokers == 5:
            max_number = 0
        else:
            max_number = numbers[0][1] if numbers[0][0] != 'A' else numbers[1][1]
        
        if max_number  + jokers  == 5:
            return 'five'
        if max_number  + jokers == 4:
            return 'four'
        if max_number  + jokers == 3 and numbers[1][1] == 2:
            return 'full'
        if max_number  + jokers == 3 and numbers[1][1] == 1:
            return 'three'
        if max_number  + jokers == 2 and numbers[1][1] == 2:
            return 'two'
        if max_number  + jokers == 2 and numbers[1][1] == 1:
            return 'one'
        if max_number  + jokers == 1:
            return 'high'

        return 'otro'
    
    def get_total_winnings_with_joker(self, path:str)-> int:

        hands = self._load_data_with_joker(path)
        total_winnings = 0
        sorted_bids = list()
        hand_types = dict()

        
        for cards,bid, original in hands:
            hand_type = self._get_hand_type_with_joker(cards)
            current_list = hand_types.get(hand_type, list())
            current_list.append((cards,bid, original))
            hand_types[hand_type] = current_list
        

        
        bids = hand_types.get('high',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('one',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('two',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('three',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('full',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('four',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        bids = hand_types.get('five',list())
        sorted_bids.extend(sorted(bids,key=lambda x: x[0]))
        
        for pos, bid in enumerate(sorted_bids,1):
            total_winnings +=  pos * bid[1]

        return total_winnings




            




