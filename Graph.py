# Name: Ankit Vaity
# ID: 801203693
# Email: avaity@uncc.edu
# Start Command: python3 Graph.py network.txt

import heapq
import sys
from decimal import Decimal

class Vertex:
    def __init__(self, name):
        self.name = name 
        self.adj =  {}
        self.cost = float('inf')
        self.pred = None
        self.status = True
        self.visited = False

    def Vertex(self, name):
        self.name = name

    def reset(self):
        self.cost = float('inf')
        self.pred = None
        self.visited = False

class Graph:
    def __init__(self):
        self.vertexMap =  dict()

    def addEdge(self, sourceName,  destName, weight):
        source = self.getVertex(sourceName)
        dest = self.getVertex(destName)
        source.adj[dest.name] = {
            "weight": float(weight),
            "status": True
        }
    
    def deleteEdge(self, sourceName, destName):
        if sourceName in self.vertexMap:
            vertex = self.vertexMap[sourceName]
            vertex.adj.pop(destName, None)
    
    def edgeDown(self, sourceName, destName):
        if sourceName in self.vertexMap:
            vertex = self.vertexMap[sourceName]
            if destName in vertex.adj:
                vertex.adj[destName]["status"] = False
    
    def edgeUp(self, sourceName, destName):
        if sourceName in self.vertexMap:
            vertex = self.vertexMap[sourceName]
            if destName in vertex.adj:
                vertex.adj[destName]["status"] = True

    def vertexDown(self, vertexName):
         if vertexName in self.vertexMap:
            vertex = self.vertexMap[vertexName]
            vertex.status = False
    
    def vertexUp(self, vertexName):
         if vertexName in self.vertexMap:
            vertex = self.vertexMap[vertexName]
            vertex.status = True
        
    def  getVertex(self, vertexName):
        if vertexName not in self.vertexMap:
            vertex = Vertex(vertexName)
            self.vertexMap[vertexName] = vertex
        vertex = self.vertexMap[vertexName]
        return  vertex



    def findShortestPath(self, sourceName, destName):
        print()
        # Check if source vertex exists
        if sourceName in self.vertexMap:
            currentVertex = self.vertexMap[sourceName]
            currentVertex.cost = 0

            for i in range(len(self.vertexMap)-1):

                # Check if vertex is visited and up
                if not currentVertex.visited and currentVertex.status:
                    currentVertex.visited = True
                    heap = []

                    # Push neighbouring vertices into heap and run heapify 
                    for edgeName, value in currentVertex.adj.items():
                        neighbourVertex = self.vertexMap[edgeName]
                        # Check if edge and vertex is up
                        if value['status'] and not neighbourVertex.visited:
                            cost = Decimal(str(currentVertex.cost)) + Decimal(str(value['weight']))
                            if cost < neighbourVertex.cost:
                                neighbourVertex.cost = cost
                                neighbourVertex.pred = currentVertex.name
                            heapq.heappush(heap, (value['weight'], neighbourVertex.name))
                        heapq.heapify(heap)
                
                if not heap:
                    for x in self.vertexMap:
                        if not self.vertexMap[x].visited:
                            currentVertex = self.vertexMap[x]
                            break
                    continue

                # Pop vertex with lowest edge weight
                currentVertex = self.vertexMap[heapq.heappop(heap)[1]]
            
            path = [destName]
            nodeName = destName
            while True:
                node = self.vertexMap[nodeName]
                if node.pred == sourceName:
                    path.insert(0, node.pred)
                    break
                else:
                    path.insert(0, node.pred)
                    nodeName = node.pred

            print(' '.join(path).strip(), self.vertexMap[destName].cost)

            # Reset visited, pred and cost values of all vertices
            for x in self.vertexMap:
                self.vertexMap[x].reset()
        else:
            print("Please enter valid vertex name")



    def printGraph(self):
        print()
        sortedVertices = list(self.vertexMap.keys())
        sortedVertices.sort()
        for node in sortedVertices:
            vertex = self.vertexMap[node]
            if vertex.status:
                print(vertex.name)
            else:
                print(vertex.name, "DOWN")
            sortedEdges = list(vertex.adj.keys())
            sortedEdges.sort()
            for i in sortedEdges:
                if vertex.adj[i]["status"]:
                    print(" ", i, vertex.adj[i]["weight"])
                else:
                     print(" ", i, vertex.adj[i]["weight"], "DOWN")
    


    def reachableVertices(self):
        # Approach:
        # We are using Depth First Search for traversing the Graph.
        # Pick a vertex and check if its visited.
        # If it is not visited then mark it as visited by pushing the vertex in the reachable list of vertices.
        # Recursively run dfs on its adjacent vertices.
        # Repeat this process until all possible reachable vertices are visited.
        # Run the above steps iteratively for every vertex.

        # Time Complexity:
        # If there are V number of vertices and E number of edges in the dircted graph.
        # For each vertex we traverse its adjacency list once in linear time
        # The sum of the size of adjacency list of all vertices (V) is E.
        # Therefore time complexity of running dfs on a vertex is O(V)+O(E) = O(V+E)
        # We repeat the process on all the vertex in the graph.
        # Therefore, Total Time complexity  = O(V(V+E))


        print()
        def findAllReachableVertices(vertex, reachable):
            for neighbour in vertex.adj:
                # Check if neighbour is visited
                if neighbour not in reachable and neighbour != vertexName:
                    neighbourVertex = self.vertexMap[neighbour]
                    # Check if edge and vertex is up
                    if vertex.adj[neighbour]['status'] and neighbourVertex.status:
                        reachable.add(neighbour)
                        # Recursive dfs call
                        findAllReachableVertices(neighbourVertex, reachable)

        sortedVertices = list(self.vertexMap.keys())
        sortedVertices.sort()

        # Loop through all vertices
        for vertexName in sortedVertices:
            vertex = self.vertexMap[vertexName]
            # Check if vertex is up
            if vertex.status:
                reachable = set()
                # Run Depth First Search on each vertex
                findAllReachableVertices(vertex, reachable)

                print(vertex.name)
                sorted(reachable)
                reachableList = list(reachable)
                reachableList.sort()
                for node in reachableList:
                    print(" ", node)


    # Process a request
    def processRequest(self):
        try:
            print()
            query = input('Enter a Query: ')
            query = query.split(" ")
            if len(query) > 0:
                queryName = query[0]

                if queryName == 'addedge':
                    # Check for valid query parameters
                    if len(query) != 4:
                        print('Please enter valid query parameters')
                        print()
                    else:
                        try:
                            tailvertex = query[1]
                            headvertex = query[2]
                            transmit_time = float(query[3])
                            self.addEdge(tailvertex, headvertex, transmit_time)
                        except Exception as e:
                            print('Please enter valid query parameters')
                            print()

                elif queryName == 'deleteedge':
                    # Check for valid query parameters
                    if len(query) != 3:
                        print('Please enter valid query parameters')
                        print()
                    else:
                        try:
                            tailvertex = query[1]
                            headvertex = query[2]
                            self.deleteEdge(tailvertex, headvertex)
                        except Exception as e:
                            print('Please enter valid query parameters')
                            print()

                elif queryName == 'edgedown':
                    # Check for valid query parameters
                    if len(query) != 3:
                        print('Please enter valid query parameters')
                        print()
                    else:
                        try:
                            tailvertex = query[1]
                            headvertex = query[2]
                            self.edgeDown(tailvertex, headvertex)
                        except Exception as e:
                            print('Please enter valid query parameters')
                            print()

                elif queryName == 'edgeup':
                    # Check for valid query parameters
                    if len(query) != 3:
                        print('Please enter valid query parameters')
                        print()
                    else:
                        try:
                            tailvertex = query[1]
                            headvertex = query[2]
                            self.edgeUp(tailvertex, headvertex)
                        except Exception as e:
                            print('Please enter valid query parameters')
                            print()

                elif queryName == 'vertexdown':
                    # Check for valid query parameters
                    if len(query) != 2:
                        print('Please enter valid query parameters')
                        print()
                    else:
                        try:
                            vertex = query[1]
                            self.vertexDown(vertex)
                        except Exception as e:
                            print('Please enter valid query parameters')
                            print()

                elif queryName == 'vertexup':
                    # Check for valid query parameters
                    if len(query) != 2:
                        print('Please enter valid query parameters')
                        print()
                    else:
                        try:
                            vertex = query[1]
                            self.vertexUp(vertex)
                        except Exception as e:
                            print('Please enter valid query parameters')
                            print()

                elif queryName == 'path':
                    # Check for valid query parameters
                    if len(query) != 3:
                        print('Please enter valid query parameters')
                        print()
                    else:
                        try:
                            from_vertex = query[1]
                            to_vertex = query[2]
                            self.findShortestPath(from_vertex, to_vertex)
                        except Exception as e:
                            print('Please enter valid query parameters')
                            print()

                elif queryName == 'print':
                    self.printGraph()

                elif queryName == 'reachable':
                    self.reachableVertices()

                elif queryName == 'quit':
                    return

                else:
                    print("Invalid Query")
                    print()

        except Exception as e:
            print(e)
            print()
            return  False
        return  True



def main():
    g = Graph()
    fin = sys.argv[1]

    with open(fin) as f:
        lines = f.readlines()

    #  Read the edges and insert
    for line in lines:
        line = line.strip().split(" ")
        if (len(line) != 3):
            print("Skipping ill-formatted line " + line)
            continue
        vertex1 = line[0]
        vertex2 = line[1]
        weight = line[2]
        g.addEdge(vertex1, vertex2, weight)
        g.addEdge(vertex2, vertex1, weight)
    
    while g.processRequest():
        pass

if __name__=="__main__":
    main()
