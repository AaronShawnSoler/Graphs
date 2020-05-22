"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        # starting node
        q.enqueue(starting_vertex)

        # keep track of visited nodes
        visited = set()

        # while the que isn't empty
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        # starting node
        s.push(starting_vertex)

        # keep track of visited nodes
        visited = set()

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        s = Stack()
        s.push(starting_vertex)
        visited = set()

        def dft_r():
            if s.size() > 0:
                v = s.pop()
                if v not in visited:
                    print(v)
                    visited.add(v)
                    for next_vert in self.get_neighbors(v):
                        s.push(next_vert)
                dft_r()

        dft_r()

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty...
        # Dequeue the first PATH
        # Grab the last vertex from the PATH
        # If that vertex has not been visited...
        # CHECK IF IT'S THE TARGET
        # IF SO, RETURN PATH
        # Mark it as visited...
        # Then add A PATH TO its neighbors to the back of the queue
        # _COPY_ THE PATH
        # APPEND THE NEIGHOR TO THE BACK
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        path = {}
        path[starting_vertex] = None

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                if v == destination_vertex:
                    shortest_path = []
                    shortest_path.insert(0, destination_vertex)
                    curr = path[destination_vertex]
                    while curr != None:
                        print("CURR: ", curr)
                        shortest_path.insert(0, curr)
                        curr = path[curr]
                    print("SHORT: ", shortest_path)
                    print("PATH: ", path)
                    return shortest_path
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    path[next_vert] = v
                    q.enqueue(next_vert)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        s_path = {}
        s_path[starting_vertex] = None
        print(s_path)

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                if v == destination_vertex:
                    shortest_path = []
                    shortest_path.insert(0, destination_vertex)
                    curr = s_path[destination_vertex]
                    while curr != starting_vertex:
                        print("CURR: ", curr)
                        shortest_path.insert(0, curr)
                        curr = s_path[curr]
                    shortest_path.insert(0, curr)
                    print("SHORT: ", shortest_path)
                    print("PATH: ", destination_vertex, s_path)
                    return shortest_path
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    s_path[next_vert] = v
                    s.push(next_vert)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        s_path = {}
        s_path[starting_vertex] = None
        shortest_path = []

        def dts_r():
            if s.size() > 0:
                v = s.pop()
                if v not in visited:
                    if v == destination_vertex:
                        shortest_path.insert(0, destination_vertex)
                        curr = s_path[destination_vertex]
                        while curr != starting_vertex:
                            print("CURR: ", curr)
                            shortest_path.insert(0, curr)
                            curr = s_path[curr]
                        shortest_path.insert(0, curr)
                        print("SHORT: ", shortest_path)
                        print("PATH: ", destination_vertex, s_path)
                        return shortest_path
                    visited.add(v)
                    for next_vert in self.get_neighbors(v):
                        s_path[next_vert] = v
                        s.push(next_vert)
                dts_r()
        dts_r()
        return shortest_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    print(graph.get_neighbors(7))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("==== BFT ====")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("==== DFT ====")
    graph.dft(1)
    print("==== DFT_R ====")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("==== BFS ====")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("==== DFS ====")
    print(graph.dfs(1, 6))
    print("==== DFS_R ====")
    print(graph.dfs_recursive(1, 6))
