import re

class Agriculture:
    def __init__(self) -> None:
        self.seeds = list()
        self.cultivation = dict()


    def _load_data(self, path:str)-> None:

        with open(path, "r") as file:
            # Reading from a file
            line = file.readline()
            self.seeds = [int(n) for n in re.findall('\d+', line.replace('seeds:',''))]
            
            step = -1
            
            for line in file:
                if ' map:' in line:
                    # current_step = line[0:line.index(' map:')]
                    step += 1
                    self.cultivation[step] = []
                    
                elif line[0].isdigit():
                    dst_start, src_start, offset = [int(n) for n in re.findall('\d+',line)]
                    self.cultivation[step].append((dst_start, src_start, offset))   


    def get_min_location(self, path:str)-> int:

        self._load_data(path)
        
        locations = list()

        for seed in self.seeds:
            location = seed 
            for step in range(0,7):
                for dst, src, offset in self.cultivation[step]:
                    if src <= location < src + offset:
                        location = dst + (location - src)
                        break
            locations.append(location)

            
        return min(locations)
    



