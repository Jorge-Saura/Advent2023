import re

class Maze:

    def _load_data(self, path:str)-> list:
        maze = list()
        start = None

        with open(path, "r") as file:
            for y,line in enumerate(file,0):
                maze.append(line.replace('\n',''))
                x = line.find('S')
                if x != -1:
                    start = (x,y)
                
        return [start, maze]
    
    def _get_surrounding_points(self,point:tuple,max_x:int, max_y:int) -> list:

        points = list()

        x,y = point

        points = [(x-1,y-1),(x,y-1),(x+1,y-1),
                  (x-1,y),(x+1,y),
                  (x-1,y+1),(x,y+1), (x+1,y+1)]

        return [n for n in points if n[0]>=0 and n[0]< max_x and n[1] >=0 and n[1]<max_y] 

    def _get_connectors(self, start:tuple,grid:list)-> list:

        x,y = start
        symbol = grid[y][x]
        

        if symbol == '.':
            return []
        if symbol == '7':
            left = (x-1, y)
            down = (x, y+1)
            return [left,down]
        if symbol == '|':
            top = (x, y-1)
            down = (x, y+1)
            return [top,down]
        if symbol == 'J':
            top = (x, y-1)
            left = (x-1, y)
            return [top,left]
        if symbol == '-':
            left = (x-1, y)
            right = (x+1, y)
            return [left,right]
        if symbol == 'L':
            top = (x, y-1)
            right = (x+1, y)
            return [top,right]
        if symbol == 'F':
            right = (x+1, y)
            down = (x, y+1)
            return [right,down]

        if symbol == 'S':
            #find al the possible connectors
            surounding_points = self._get_surrounding_points(start,len(grid[0]), len(grid))
            connectors = list()
            for p in surounding_points:
                current_connectors = self._get_connectors(p,grid)
                if start in current_connectors:
                    connectors.append(p)
            return connectors

        return []
    


    def get_max_distance(self, path:str) -> int:

        start, maze = self._load_data(path)

        first_way = dict()
        second_way = dict()

        max_distance = 0
        visited_points = dict()
        
        current_point = start
        f_current, s_current = self._get_connectors(start,maze)
        first_way[start] = 0
        first_way[f_current] = 1
        second_way[start] = 0
        second_way[s_current] = 1
        distance = 1
        while first_way.get(s_current,0) == 0 and second_way.get(f_current,0) == 0:
            distance += 1
            f_points = self._get_connectors(f_current,maze)
            f_current = f_points[0] if first_way.get(f_points[0],-1) == -1 else f_points[1]
            first_way[f_current] = distance

            s_points = self._get_connectors(s_current,maze)
            s_current = s_points[0] if second_way.get(s_points[0],-1) == -1 else s_points[1]
            second_way[s_current] = distance

        
        return max(first_way.values())