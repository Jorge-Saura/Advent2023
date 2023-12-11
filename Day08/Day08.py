from functools import reduce
from collections import Counter
import re

class NetworkNavigator:

    def _load_data(self, path:str)-> list:
        steps = str
        nodes = dict()

        with open(path, "r") as file:
            # Reading from a file
            steps = file.readline().strip('\n')
            empty_line = file.readline()

            for line in file:
                key, values = line.strip('\n').split(' = ')
                values = values.strip('()')
                values = [n for n in values.split(', ')]
                nodes[key] = values

        return [steps,nodes]
    
   
    
    def get_number_of_steps(self, path:str)-> int:

        steps, nodes = self._load_data(path)

        number_of_steps = 0
        current_node = 'AAA'
        total_steps = len(steps)

        while current_node != 'ZZZ':
            current_step = steps[number_of_steps%total_steps]
            current_node = nodes[current_node][0] if current_step == 'L' else nodes[current_node][1]
            number_of_steps += 1



 
        return number_of_steps




            




