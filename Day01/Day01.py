class Calibrator:

    def _read_data(self, path:str)-> list[str]:
        result = []
        with open(path, "r") as file:
            # Reading from a file
            result = [line.rstrip() for line in file]

        return result
    

    def _get_first_digit(self, line:str) -> int:
        dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

        first_number, first_number_position = next(((char,pos) for pos,char in enumerate(line) if char.isdigit()), (None,None))
        char_digits = [(value, line.find(key)) for key,value in dict.items()]
        char_digits = [(value, pos) for value,pos in char_digits if pos >-1]
        if first_number:
            char_digits.append((int(first_number), first_number_position))

        first_digit, _ = min(char_digits,key= lambda pair: pair[1])

        return first_digit

    def _get_last_digit(self, line:str) -> int:
        reverse_line = line[::-1]
        dict = {'eno':1, 'owt':2, 'eerht':3, 'ruof':4, 'evif':5, 'xis':6, 'neves':7, 'thgie':8, 'enin':9}

        first_number, first_number_position = next(((char,pos) for pos,char in enumerate(reverse_line) if char.isdigit()), (None,None))
        char_digits = [(value, reverse_line.find(key)) for key,value in dict.items()]
        char_digits = [(value, pos) for value,pos in char_digits if pos >-1]
        if first_number:
            char_digits.append((int(first_number), first_number_position))

        last_digit, _ = min(char_digits,key= lambda pair: pair[1])

        return last_digit
        
    def _process_line(self, line:str)-> int:
        
        first_digit = next(n for n in line if n.isdigit())
        last_digit = next(n for n in reversed(line) if n.isdigit())

        return (int(first_digit)*10) + int(last_digit)


    def _process_line_2(self, line:str)-> int:
        
        first_digit = self._get_first_digit(line)
        last_digit = self._get_last_digit(line)

        return (first_digit*10) + last_digit
    

    def get_calibrator_code (self, path:str)-> int:
        
        calibrator_code = 0 
        lines = self._read_data(path)

        for line in lines:
            line_number = self._process_line(line)
            calibrator_code += line_number

        return calibrator_code
    

    def get_calibrator_code_2 (self, path:str)-> int:
        
        calibrator_code = 0 
        lines = self._read_data(path)

        for line in lines:
            line_number = self._process_line_2(line)
            calibrator_code += line_number

        return calibrator_code

