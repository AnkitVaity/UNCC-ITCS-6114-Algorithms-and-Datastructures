ITCS 6114 - Algorithms and Data Structures
Project 1

Name: Ankit Vaity
ID: 801203693
Email: avaity@uncc.edu

Programming Language: python3
IDE Used: Visual Studio Code

Start Script: python3 Graph.py network.txt

Project Tasks:
    1. Build the initial graph.
    2. Update the graph.
    3. Fine the shortest path between any two vertices in the graph based on its current state. 
    4. Fine reachable sets of vertices.
    5. Printing the graph.

How To Use:
    1. When you run the start Script the program will tell you to Enter a query.
    2. Type any query from the query list give below to perform respective tasks on the qraph.

Query List:
    1. addedge tailvertex headvertex transmit_time: Add a single directed edge from tailvertex to headvertex with transmit_time as the weight of the edge.
    2. deleteedge tailvertex headvertex: Delete the specified directed edge from the graph.
    3. edgedown tailvertex headvertex: Mark the directed edge as “down” and unavailable for use.
    4. edgeup tailvertex headvertex: Mark the directed edge as “up”, and available for use.
    5. vertexdown vertex: Mark the vertex as “down”.
    6. vertexup vertex: Mark the vertex as “up” again.
    7. path from_vertex to_vertex: Compute shortest path from from_vertex to to_vertex.
    8. reachable: Print the set of vertices reachable from each vertex.
    9. print: Print the contents of the graph.
    10. quit: Quit the program.

Program Design:
    Class:
        1. Vertex Class: Used to store the information of the vertex in the graph.
            Variables: 
                name (String) representing the name of the vertex, 
                adj (Dictionary) containing the list of neighbors of the vertex.
                status (Boolean) represents if the vertex is up or down.
                cost (Float) containing the cost of the vertex.
                pred (String) represents the name of the predecessor vertex.
                visited (Boolean) represents if the vertex is visited or not. 
            Functions:
                reset: The reset function resets the value of cost, pred and visited variables to default.

        2. Graph Class: Used to create and edit the graph and perform certain tasks on the graph.
            Variables:
                vertexMap (Dictionary) representing the set of Vertex objects forming the graph.
            Functions:
                i.    getVertex: 
                        - takes the vertex name as input and checks if the vertex exists in vertexMap. 
                        - If the vertex is not in vertexMap it creates a new vertex object with the input vertex name and adds the vertex to the vertexmap.
                ii.   addEdge: 
                        - takes head vertex name, tail vertex name and the edge weight as input.
                        - It first checks if the head vertex and tail vertex exists in vertexMap 
                        - and if it does then adds the tail vertex in the adjacency list of the source vertex.
                iii.  deleteEdge: 
                        - takes head vertex name and tail vertex as input and checks if the head vertex exists in vertexMap.
                        - and if it does then removes the tail vertex from the adjacency list of the head vertex.
                iv.   edgedown: 
                        - takes head vertex name and tail vertex as input and checks if the head vertex exists in vertexMap.
                        - and next it checks if the tail vertex is in the adjacency list of the head vertex and sets the status of the edge to False.
                v.    edgeup: 
                        - takes head vertex name and tail vertex as input and checks if the head vertex exists in vertexMap.
                        - and next it checks if the tail vertex is in the adjacency list of the head vertex and sets the status of the edge to True.
                vi.   vertexDown: 
                        - takes vertex name as input and checks if the vertex exists in the vertexMap.
                        - and if it does then set the status of the vertex object to False.
                vii.  vertexUp: 
                        - takes vertex name as input and checks if the vertex exists in the vertexMap.
                        - and if it does then set the status of the vertex object to True.
                viii. findShortestPath: 
                        - takes source and destination vertex names as inputs.
                        - First it checks if the source vertex exists in vertexMap and if it does then it sets the current vertex to the source vertex.
                        - Next it sets the cost of source vertex to 0 and sets visited to True.
                        - Then initialize a min heap and loops through all the edges in the adjacency list of the current vertex.
                        - If the neighboring vertex is not visited and and the neighboring vertex and edge is up and the cost of neighboring vertex 
                        - if more than the sum of the edge weight and cost of current vertex,
                        - then it sets the cost of the neighboring edge to the sum of the edge weight and cost of current vertex.
                        - Next it adds the neighboring vertex and its edge weight to the min heap.
                        - Once all neighbor costs are updated it sets the current vertex to the vertex with lowest cost in the min heap 
                        - and repeats the above step till all the vertices are visited.
                        - The function returns a list of vertices which representing the path to reach to destination vertex from source vertex using the predecessor vertex 
                        - and print the updated cost of the destination vertex.
                ix.   printGraph: 
                        - sort all the vertices in the vertexMap alphabetically 
                        - and loops through the vertexMap and prints the vertex name and print DOWN if the status of vertex is set to false.
                        - Next it sorts the neighboring vertices in the adjacency list of the vertex and prints the name of the neighboring vertex 
                        - and the cost of the edge and print DOWN if the status of edge is set to false.
                        - Repeats the above steps for all the vertices.
                x.    reachableVertices: 
                        - sort all the vertices in the vertexMap alphabetically and loop through each vertex in vertexMap and check if the vertex is UP.
                        - If the current vertex is UP the run DFS on the current vertex and check if the neighboring vertex is in reachable list 
                        - and if its not then add the neighboring vertex in the reachable list and run DFS on its adjacent vertices.
                        - Repeat the above steps until all possible reachable vertices are visited.
                        - Run the above steps iteratively for every vertex.
                xi.   processRequest: 
                        - This function is used to take queries as input from the user and checks if the query is valid 
                        - and run the function associated with the query.
                
    Main Function: 
        i.   In the main function we create an instance of the graph class
        ii.  Read the command line arguments containing the text file with graph structure and loop through the text file to initialize the graph.
        iii. Next we run the processRequest function of the graph object to take inputs form user to perform certain tasks on the graph.

Data Structure Design:
      Data Structures Used - Graph, Heap and Stack
      1. The data communication network is modeled using Graph data structure with set of vertices connected with weighted directed edge. Where the weight of the edge corresponds to time taken for data transmission from the vertex at one end to the vertex at the other end. 
      2. To compute the best path to reach the destination node we are using Dijkstra’s algorithm, which is implemented using a priority queue as Min Heap data structure which is used to find the edge with lowest weight from a vertex.
      3. To find all the reachable vertices we are using Depth First Search which is implemented using Stack data structure. First visited vertices are pushed into the stack and second if there is no vertices then visited vertices are popped.

Summary: Successfully implemented all the five tasks in this project i.e. building the initial graph, updating the graph to reflect changes, finding the shortest path between any two vertices in the graph based on its current state, printing the graph, and finding reachable sets of vertices.
        
                      


