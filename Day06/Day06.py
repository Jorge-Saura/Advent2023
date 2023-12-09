from functools import reduce
import re

class BoatRace:

    def _load_data(self, path:str)-> None:
        times = None
        distances = None

        with open(path, "r") as file:
            # Reading from a file

            line = file.readline()
            times = [int(n) for n in re.findall('\d+',line)]
            line = file.readline()
            distances = [int(n) for n in re.findall('\d+',line)]

        return {key:value for key,value in zip(times, distances)}
    
    def _get_times_higher_distances(self, time:int, distance:int) -> list:
        greater_values = list()

        for t in range(1,time):
            if (time-t) * t > distance:
                greater_values.append(t)
        
        return greater_values

    def get_good_times(self, path:str) -> int:
        races = self._load_data(path)
        total_times = list()

        for time,distance in races.items():
            good_times = self._get_times_higher_distances(time,distance)
            total_times.append(len(good_times))

        return reduce(lambda x,y: x * y, total_times)





            




