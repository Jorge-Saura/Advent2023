class CubeGame:

    def _read_data(self, path:str)-> list[str]:
        result = []
        with open(path, "r") as file:
            # Reading from a file
            result = [line.rstrip() for line in file]

        return result
           
    def _process_line(self, line:str)-> dict:
        # position is Red, Green, Blue
        dictionary = {'red':0, 'green': 0, 'blue':0}

        rows = (line.rsplit(':', 1)[1]).split(';')
        for row in rows:
            cubes = row.split(',')
            for cube in cubes:
                
                number, color = cube.strip().split(' ')
                number = int(number.strip())
                color  = color.strip()
                dictionary[color] = number if number > dictionary[color] else dictionary[color]
        
        return dictionary




    
    def get_good_games(self, path:str)-> int:
        
        max_cubes = dictionary = {'red':12, 'green': 13, 'blue':14}

        sum_good_games = 0 
        lines = self._read_data(path)

        for num, line in enumerate(lines,1):
            dictionary = self._process_line(line)
            sum_good_games = sum_good_games + num if dictionary['red'] <= max_cubes['red'] \
                                                and dictionary['green'] <= max_cubes['green'] \
                                                and dictionary['blue'] <= max_cubes['blue'] else sum_good_games

        return sum_good_games
