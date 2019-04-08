"""
Simple graph implementation
"""


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size()>0:
            return self.queue.pop(0)
        else: 
            return None
    def size(self):
        return len(self.queue)        

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        #pass  # TODO
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_directed_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            self.vertices[vertex_1].add(vertex_2)
        else: 
            raise IndexError("That vertex does not exist")  

    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            self.vertices[vertex_1].add(vertex_2)
            self.vertices[vertex_2].add(vertex_1)
        else:
            raise IndexError("That vertex does not exist")               

    def bft(self, starting_vertex_id):
        #create an empty queue
        q = Queue()

        visited = set()
        # #create a visited set
        # Engugue the starting vertex to the queue
        q.enqueue(starting_vertex_id)
        # #while the queue  is not empty...
        while q.size() > 0:
            v = q.dequeue()
        # Dequeue the first element from the queue 
         
        #check if it's visit
        # If it hasn't been visited
        if v not in visited:
            #mark is as visited
            print(v)  
            visited.add(v)
            #Put all its neghbors in the back of the queue
            for next_vert in self.vertices[v]:
                q.enqueue(next_vert)    

    def bfs(self, starting_vertex_id, target_vertex):
        # Create an empty queue
        q = Queue()
            

        # Create a visited set
        visited = []
        # Enqueue [A PATH TO] the starting vertex to the queue
        q.enqueue([starting_vertex_id])
        # While the queue is not empty...
        while q.size() > 0:
           # Dequeue the first [PATH] from the queue
            path = q.dequeue()
           # PULL THE LAST VERTEX FROM THE PATH
            node = path[-1] #last vertex from the path
           # Check if it's visited
            if node not in visited:
           # If it hasn't been visited...
           # Mark it as visited
                print(node)
                visited.append(node)
                # CHECK IF IT'S EQUAL TO THE TARGET VERTEX 
                if node == target_vertex:
                # IF IT IS, RETURN THE PATH        
                    return path
            
                # Put [A PATH TO] all of its neighbors in the back of the queue
                for next_vertex in self.vertices[node]:
                    # COPY THE PATH
                    new_path = path.copy()
                    # APPEND THE NEIGHBOR VERTEX TO THE PATH
                    new_path.append(next_vertex)
                    # ENQUEUE THE NEW PATH   
                    q.enqueue(new_path) 
        return False                