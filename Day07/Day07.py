from functools import reduce
import re

class CamelCards:

    def _load_data(self, path:str)-> list:
        
        hands = list()
        with open(path, "r") as file:
            # Reading from a file

            line = file.readline()
            cards, bid = line.replace('\n','').split(' ')
            hands.append((cards,int(bid)))

  
        return hands
    






            




