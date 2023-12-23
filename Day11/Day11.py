
class CosmicExpansion:

    def _load_data(self, path:str)-> list:
        universe = list()

        with open(path, "r") as file:
            # Reading from a file
            for line in file:
            
                line = line.strip('\n')
                universe.append(line)

        return universe
    
    def _get_horizontal_empty_lines(self, grid:list) -> list:

        empty_lines = list()
        for idx, line in enumerate(grid):
            if all((n == '.' for n in line)):
                empty_lines.append(idx)

        return empty_lines
    
    def _get_vertical_empty_lines(self, grid:list) -> list:

        grid_trasposed = list(map(''.join, zip(*grid)))
        
        return self._get_horizontal_empty_lines(grid_trasposed)

    def _add_horizontal_line(self, grid:list, index:int) -> list:

        augmented_grid = grid.copy()
        new_line = '.'*len(augmented_grid[0])
        augmented_grid.insert(index, new_line)

        return augmented_grid
    
    def _add_vertical_line(self, grid:list, index:int) -> list:

        augmented_grid = list(map(''.join, zip(*grid)))
        new_line = '.'*len(augmented_grid[0])
        augmented_grid.insert(index, new_line)
        augmented_grid = list(map(''.join, zip(*augmented_grid)))

        return augmented_grid


    def _get_galaxies(self, grid:list) -> list:

        galaxies = list()
        for y,line in enumerate(grid):
            for x, c in enumerate(line):
                if c == '#':
                    galaxies.append((x,y))

        return galaxies
    
    def _get_distance(self, a:tuple, b:tuple) -> int:

        return abs(b[0]-a[0]) + abs(b[1]-a[1])  
        

    def get_shortest_paths(self, path:str) -> int:

        grid = self._load_data(path)

        hor_lines = self._get_horizontal_empty_lines(grid)
        ver_lines = self._get_vertical_empty_lines(grid)

        offset = 0
        for y in hor_lines:
            grid = self._add_horizontal_line(grid,y + offset)
            offset += 1
        
        offset = 0
        trasposed_grid  = list(map(''.join, zip(*grid)))
        for y in ver_lines:
            trasposed_grid = self._add_horizontal_line(trasposed_grid,y + offset)
            offset += 1

        grid = list(map(''.join, zip(*trasposed_grid)))

        galaxies = self._get_galaxies(grid)


        shortests_paths =list()

        for pos, galaxy in enumerate(galaxies):
            paths = list()   
            for other_galaxy in galaxies[pos+1:]:
                paths.append(self._get_distance(galaxy, other_galaxy))

            if paths:
                shortests_paths.append(sum(paths))

            


        return sum(shortests_paths)
            


    def get_shortest_paths2(self, path:str, distance:int) -> int:

        grid = self._load_data(path)

        hor_lines = self._get_horizontal_empty_lines(grid)
        ver_lines = self._get_vertical_empty_lines(grid)

        galaxies = self._get_galaxies(grid)

        shortests_paths =list()

        for pos, galaxy in enumerate(galaxies):
            paths = list()   
            for other_galaxy in galaxies[pos+1:]:
                initial_distance = self._get_distance(galaxy, other_galaxy)
                min_x_galaxy = min(galaxy[0],other_galaxy[0])
                max_x_galaxy = max(galaxy[0],other_galaxy[0])
                for n in ver_lines:
                    if  min_x_galaxy < n < max_x_galaxy:
                        initial_distance += distance - 1

                min_y_galaxy = min(galaxy[1],other_galaxy[1])
                max_y_galaxy = max(galaxy[1],other_galaxy[1])
                for n in hor_lines:
                    if  min_y_galaxy < n < max_y_galaxy:
                        initial_distance += distance - 1 
                paths.append(initial_distance)

            if paths:
                shortests_paths.append(sum(paths))

            


        return sum(shortests_paths)
            


