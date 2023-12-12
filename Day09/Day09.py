import re

class Mirage:

    def _load_data(self, path:str)-> list:
        series = list()

        with open(path, "r") as file:
            for line in file:
                numbers = re.findall('-?(?:\d+,?)+',line)
                series.append([int(n) for n in numbers])

        return series
    

    def _get_differences(self, serie:list)-> list:

        return [serie[i + 1] - serie[i] for i in range(0,len(serie)-1)]

    def _get_next_number(self, elements:list, differences:list) -> int:
        next_sum = elements.pop(0) + differences.pop(0)
        while elements:
            next_sum = elements.pop(0) + next_sum
            
        return next_sum
    
    def _get_previous_number(self, elements:list, differences:list) -> int:
        next_sum = elements.pop(0) - differences.pop(0)
        while elements:
            next_sum = elements.pop(0) - next_sum
            
        return next_sum

    def get_next_right_numbers(self, path:str) -> int:
        series = self._load_data(path)

        sum_next_numbers = 0

        for serie in series:
            
            current_serie = serie
            last_elements = list()
            last_difference = list()
            while any(current_serie):
                last_elements.insert(0,current_serie[-1])
                current_serie = self._get_differences(current_serie)
                last_difference.insert(0,current_serie[-1])
            
            sum_next_numbers += self._get_next_number(last_elements,last_difference)

        return sum_next_numbers
   
    def get_next_left_numbers(self, path:str) -> int:
        series = self._load_data(path)

        sum_next_numbers = 0

        for serie in series:
            
            current_serie = serie
            last_elements = list()
            last_difference = list()
            while any(current_serie):
                last_elements.insert(0,current_serie[0])
                current_serie = self._get_differences(current_serie)
                last_difference.insert(0,current_serie[0])
            
            sum_next_numbers += self._get_previous_number(last_elements,last_difference)

        return sum_next_numbers

