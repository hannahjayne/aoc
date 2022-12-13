import numpy as np 
from collections import defaultdict 

FILE = "input-22_12"

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    #creates an edge
    def add_edge(self, from_node, to_node):
        self.graph[from_node].append(to_node)

    #task 1: gets shortest distance using bfs 
    def shortest_path(self, start, end):
        queue = [start]  
        visited = set(start) #nodes already visited
        distance = 0 #distance travelled

        while queue:
            for i in range(0, len(queue)):
                current_vertex = queue.pop(0)
                
                for adjacent in self.graph[current_vertex]:
                    if adjacent == end: return distance + 1
                    elif adjacent not in visited:
                        visited.add(adjacent)
                        queue.append(adjacent)
                        
            distance += 1  
            
        return None #no path found    
        
    
#opens file and builds height map as np array; also gets source and sink
def get_height_map(file_name = FILE):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    
    height_map = np.array([[get_elevation(height) for height in line[:-1]] for line in lines])
    
    #gets source and sink and then sets them to appropriate vals 
    source, sink = np.where(height_map == 0), np.where(height_map ==27)
    height_map[source[0][0]][source[1][0]], height_map[sink[0][0]][sink[1][0]] = 1, 26
     
    return height_map, (source[0][0],source[1][0]), (sink[0][0], sink[1][0]) 


#gets elevation, to create height map; uses ord() to put the letters on a scale
def get_elevation(letter):
    if letter == "S": return 0 #start; otherwise same as "a" (i.e 1)
    elif letter== "E": return 27  #end; otherwise same as "z" (i.e, 26)
    else: return ord(letter) - 96


#builds graph out of height_map array, by checking each vertex
def build_graph(height_map):
    
    graph = Graph()
    
    for row in range(0, height_map.shape[0]):
        for col in range(0, height_map.shape[1]):            
            
            if col < height_map.shape[1]-1:   
                if height_map[row][col+1] - 1 <= height_map[row][col]: #compare w. to right
                    graph.add_edge((row, col), (row, col+1))
                     
            if col > 0:  # checks not leftmost
                if height_map[row][col-1] - 1 <= height_map[row][col]:  # compare w. row to left
                    graph.add_edge((row, col), (row, col-1))
                   
            if row > 0:  # checks not top
                if height_map[row-1][col] - 1 <= height_map[row][col]:  # compare w. row above
                    graph.add_edge((row, col), (row-1, col))
                    
            if row < height_map.shape[0] - 1:  # checks not bottom
                if height_map[row+1][col] - 1 <= height_map[row][col]:  # compare w. row below
                    graph.add_edge((row, col), (row+1, col))
    return graph
    
#gets shortest path distance from S to E 
def task_one(file_name = FILE):
    height_map, source, sink = get_height_map(file_name)
    graph = build_graph(height_map) 
    shortest_path = graph.shortest_path(source, sink)
    
    print(f"Task one: {shortest_path} steps")
    
# gets shortest path distance to E from any a.
def task_two(file_name = FILE):
    height_map, source, sink = get_height_map(file_name)
    graph = build_graph(height_map) 
    
    a_locations, min_path = np.where(height_map == 1), height_map.size

    #... im so sorry dijkstra. 
    for a in range(0, len(a_locations[0])): 
        path_length = graph.shortest_path((a_locations[0][a], a_locations[1][a]), sink)
        if path_length: min_path = path_length if path_length < min_path else min_path

    print(f"Task two: {min_path} steps")
