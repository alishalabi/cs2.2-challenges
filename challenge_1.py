# Graph() #creates a new, empty graph.
# addVertex(vert) #adds an instance of Vertex to the graph.
# addEdge(fromVert, toVert) #Adds a new, directed edge to the graph that connects two vertices.
# addEdge(fromVert, toVert, weight) #Adds a new, weighted, directed edge to the graph that connects two vertices.
# getVertex(vertKey) #finds the vertex in the graph named vertKey.
# getVertices() #returns the list of all vertices in the graph.
# getNeighbors(x) # lists all vertices y such that there is an edge from the vertex x to the vertex y;


class Vertex(object):
    def __init__(self, id):
        # Initialize empty dictionary of adjacent vertex
        # The keys will be vextex, the values will be weights
        # If additional properties are needed, we might change to arrays for values
        self.adjacent_vertices = {}
        self.id = id

    def addNeighbor(self, vertex, weight=None):
        # Check to see if node already exists in dictionary
        if vertex not in self.adjacent_vertices:
            # Set node key and value in dictionary
            self.adjacent_vertices[vertex] = weight

    def getNeighbors(self):
        return self.adjacent_vertices.items()
        # print(self.adjacent_vertex.items())


class Graph:
    def __init__(self):
        self.all_vertices = {}

    def addVertex(id):
        if id not in self.all_vertices:
            new_vertex = Vertex(id)
            all_vertices.update(new_vertex)

    def addEdge(vertex1, vertex2, weight=None):
        self.all_vertices[vertex1].addNeighbor(vertex2, weight)

    def getVertex(id):
        return self.all_vertices[id]

    def getVertices():
        return self.all_vertices.items()

    def getNeighbors(id):
        return self.all_vertices[id].getNeighbors()


# node1 = Vertex()
# node2 = Vertex()
#
# node1.addVertex(node2)
# node1.get_adjacent_vertex()
