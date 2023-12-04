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

