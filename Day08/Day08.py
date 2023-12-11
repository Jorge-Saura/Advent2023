import math

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
    
    def _get_nodes_ending_with_char(self, nodes:list, ending_char:str) -> list():
        return [n for n in nodes if n[-1] == ending_char]


    def _get_number_of_steps(self, steps:str, nodes:dict, start_node:str, end_node:str) -> int:
        number_of_steps = 0
        current_node = start_node
        total_steps = len(steps)

        while current_node != end_node:
            current_step = steps[number_of_steps%total_steps]
            current_node = nodes[current_node][0] if current_step == 'L' else nodes[current_node][1]
            number_of_steps += 1
        
        return number_of_steps

    def get_number_of_steps_multiple_starts(self, path:str)-> int:

        steps, nodes = self._load_data(path)

        number_of_steps = 0
        starting_nodes = self._get_nodes_ending_with_char(nodes.keys(),'A')
        
        
        node_costs = dict()
        node_cicles = {n:0 for n in starting_nodes}
        node_step = {n:n for n in starting_nodes}
        node_endings = {n:list() for n in starting_nodes}
        total_steps = len(steps)

        while not all(n for n in node_cicles.values()): #all starting nodes have a cicle
            for start_node in starting_nodes:
                current_step = steps[number_of_steps%total_steps]
                
                
                node_step[start_node] = nodes[node_step[start_node]][0] if current_step == 'L' else nodes[node_step[start_node]][1]
                if node_step[start_node][-1] == 'Z':
                    node_cicles[start_node] = node_cicles[start_node] + 1
                    node_endings[start_node].append(number_of_steps + 1)
                
            number_of_steps += 1
        
        lcm_value = math.lcm(*[n[0] for n in node_endings.values()])
 
        return lcm_value




            




