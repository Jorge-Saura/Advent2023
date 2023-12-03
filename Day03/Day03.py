class GearRatios:

    def _read_data(self, path:str)-> list[str]:
        result = []
        with open(path, "r") as file:
            # Reading from a file
            result = [line.rstrip() for line in file]

        return result

    def _get_numbers_in_line(self, line:str) -> list[tuple]:
        numbers_in_line = list()
        
        digit = ''
        start_pos = -1
        end_pos = -1
        in_digit = 0
        for pos,c in enumerate(line,0):
            if c.isdigit(): 
                start_pos = pos if start_pos == -1 else start_pos
                end_pos = pos
                digit = digit + c
                in_digit = 1
            else:
                if in_digit:
                    numbers_in_line.append((int(digit),start_pos,end_pos))
                    in_digit = 0
                    digit = ''
                    start_pos = end_pos = -1
        if in_digit:
            numbers_in_line.append((int(digit),start_pos,end_pos))

        return  numbers_in_line








    
    def get_gear_ratios(self, path:str)-> int:
        ratios = 0

        lines = self._read_data(path)
        min_line = 0
        max_line = len(lines) - 1
        min_char = 0
        max_char = len(lines[0]) - 1

        for num_line, line in enumerate(lines,0):
            numbers_in_line = self._get_numbers_in_line(line)
            i=0
            for number in numbers_in_line:
                min_horizontal = max(min_char, number[1] - 1)
                max_horizontal = min(max_char, number[2] + 1)
                min_vertical = max(min_line, num_line - 1)
                max_vertical = min(max_line, num_line + 1)

                top_chars = ''
                middle_chars = ''
                bottom_chars = ''

                if num_line > min_line:
                    top_chars = lines[num_line - 1][min_horizontal:max_horizontal + 1]
                
                if num_line < max_line:
                    bottom_chars = lines[num_line + 1][min_horizontal:max_horizontal + 1]

                middle_chars = line[number[1]-1] if number[1] > min_char else '' 
                middle_chars = middle_chars + line[number[2] + 1] if number[2] < max_char else ''

                all_possible_chars = top_chars + middle_chars + bottom_chars
                if any(char not in '0123456789.' for char in all_possible_chars):
                    ratios += number[0]







        return ratios
    


