from collections import Counter
import re

class Scratchcards:

    def _read_data(self, path:str)-> list[str]:
        result = []
        with open(path, "r") as file:
            # Reading from a file
            result = [line.rstrip() for line in file]

        return result

    def _get_numbers_in_line(self, line:str) -> dict:
        numbers_in_line = dict()

        _, clean_line = line.split(': ')
        clean_line = clean_line.replace('| ','')
        numbers = re.findall(r'\d+', clean_line)
        
        numbers_in_line = dict(Counter([int(n) for n in numbers]))

        return  numbers_in_line

    def get_cards_points(self, path:str)-> int:

        lines = self._read_data(path)
        cards_points  = 0

        for line in lines:
            numbers_in_line = self._get_numbers_in_line(line)
            total_winning_numbers = len([n for n,v in numbers_in_line.items() if v > 1])
            cards_points = (cards_points + pow(2,total_winning_numbers-1)) if total_winning_numbers != 0 else cards_points
            
        return int(cards_points)
    
    def _add_copy_cards(self, cards:dict, starting_card: int, next_cards_win:int, num_copies_starting_card: int)-> dict:

        for i in range(starting_card , starting_card + next_cards_win):
            cards[i]= cards.get(i,0) + (1 * num_copies_starting_card)
          
        
        return cards


    def get_cards_points_2(self, path:str)-> int:

        lines = self._read_data(path)
        cards  = dict()

        for pos, line in enumerate(lines,1):
            cards[pos] = cards.get(pos,0) + 1 # Actual card
            numbers_in_line = self._get_numbers_in_line(line)
            next_cards_to_add = len([n for n,v in numbers_in_line.items() if v > 1]) 
            cards = self._add_copy_cards(cards, pos + 1, next_cards_to_add, cards[pos])


        total_cards = sum((value for key,value in cards.items())) 
            
        return total_cards


