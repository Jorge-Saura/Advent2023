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


    def _compose_range(self, rng1: tuple, rng2: tuple) -> list:
        composed_range = list()
        c_src, c_offset = rng1    
        dst, src, offset = rng2

        if (c_src + c_offset - 1) < src: # fuera del intervalo por la izquierda
            composed_range.append((c_src, c_offset,'original')) 
        if c_src < src and src <= (c_src + c_offset - 1) <= (src + offset - 1): # fuera por la izquierda dentro por la derecha
            composed_range.append((c_src, (src -c_src),'original'))
            composed_range.append((dst, c_offset - (src - c_src),'transformed'))
        if  src <= c_src and (c_src + c_offset) <= (src + offset) : # dentro la izquierda dentro por la derecha
            composed_range.append((dst + (c_src - src), c_offset,'transformed'))
        if  src <= c_src <= src + (offset -1) and (c_src + c_offset) > (src + offset) : # dentro la izquierda fuera por la derecha
            composed_range.append((dst + (c_src - src), (src + offset) - c_src,'transformed'))
            composed_range.append((( src + offset ),  (c_src + c_offset) - (src + offset),'original'))
        if c_src > src + (offset - 1): # fuera del intervalo por la derecha
            composed_range.append((c_src, c_offset,'original')) 
        if c_src < src and src + offset < c_src + c_offset: #fuera por la izqd y fuera por la derecha (el intervalo a comprobar está dentro del intervalo actual)
            composed_range.append((c_src, (src -c_src),'original'))
            composed_range.append((dst, offset,'transformed'))
            composed_range.append((src + offset, (c_src + c_offset) - (src + offset),'original'))

        return composed_range


    def get_min_location_2(self, path:str)-> int:

        self._load_data(path)
        
        locations = list()

        seeds_ranges =[(self.seeds[i], self.seeds[i+1]) for i in range(0, len(self.seeds)-1, 2)]
        final_ranges = list()

        for seed_range  in seeds_ranges:
            original_ranges = [seed_range]
            new_ranges = list()
            checked_ranges = list()

            for step in range(0,7):
                for check_range in self.cultivation[step]:
                    while original_ranges:
                        current = original_ranges.pop(0)
                        
                        composed_ranges = self._compose_range(current,tuple(check_range))
                        checked_ranges.extend([(n[0],n[1]) for n in composed_ranges if n[2] == 'original'])
                        new_ranges.extend([(n[0],n[1]) for n in composed_ranges if n[2] == 'transformed'])
                
                    original_ranges.extend(checked_ranges)
                    checked_ranges = list()
                
                original_ranges.extend(new_ranges)
                checked_ranges = list()
                new_ranges = list()
            
            final_ranges.extend(original_ranges)

            
        return min(final_ranges,key=lambda x: x[0])[0]


