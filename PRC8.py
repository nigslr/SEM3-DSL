print("--- DFS using Adjacency Matrix ---")

vertices = ['A', 'B', 'C', 'D', 'E']

dfs_graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

dfs_visited = set()

def dfs(vertex):
    index = vertices.index(vertex)
    dfs_visited.add(vertex)
    print(vertex, end=" ")

    for i in range(len(vertices)):
        if dfs_graph[index][i] == 1 and vertices[i] not in dfs_visited:
            dfs(vertices[i])

print("DFS Traversal:")
dfs('A')
print("\n")


print("--- BFS using Adjacency List ---")

bfs_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

bfs_visited = []
queue = ['A']

print("BFS Traversal:")
while queue:
    node = queue.pop(0)

    if node not in bfs_visited:
        print(node, end=" ")
        bfs_visited.append(node)
        queue.extend(bfs_graph[node])
print("\n")

'''
--- DFS using Adjacency Matrix ---
DFS Traversal:
A B D E C 

--- BFS using Adjacency List ---
BFS Traversal:
A B C D E 


1. Aim
To Consider a particular area in your city. Note the popular locations A, B, C . . . in that area.
Assume these locations represent nodes of a graph. If there is a route between two locations,
it is represented as connections between nodes. Find out the sequence in which you will
visit these locations, starting from (say A) using (i) BFS and (ii) DFS. Represent a given
graph using an adjacency matrix to perform DFS and an adjacency list to perform BFS.

2. Objectives
1. To understand graph representation using an adjacency matrix and adjacency list.
2. To implement BFS traversal using a queue.
3. To implement DFS traversal using Stack
4. To find the sequence of visiting locations in a graph.

3. Theory
A graph is a non-linear data structure consisting of vertices (nodes) and edges (connections). In
this practical, locations in a city are represented as vertices, and roads between locations are
represented as edges.
Graph representation
 Adjacency Matrix: A two-dimensional array in which 1 indicates a connection between
two vertices and 0 indicates no connection.
 Adjacency List: Each vertex maintains a list of its adjacent vertices.
(i) Breadth First Search (BFS)
BFS visits vertices level by level, exploring all immediate neighbours before moving to the next
level. It uses a queue (FIFO).
(ii) Depth First Search (DFS)
DFS explores one path as deeply as possible before backtracking. It can be implemented using
recursion or a stack.

4. Example graph
Consider five popular locations in a city:
 A – Bus Stand

 B – Railway Station
 C – College
 D – Hospital
 E – Market
The connections between these locations are represented by the following undirected graph.
Example graph: A is the starting vertex.

5. Adjacency Matrix for DFS
Vertex A B C D E
A 0 1 1 0 0
B 1 0 0 1 1
C 1 0 0 0 0
D 0 1 0 0 0
E 0 1 0 0 0

6 . Adjacency List for BFS
Vertex Adjacent vertices
A B, C
B A, D, E
C A
D B
E B

7. Difference between BFS and DFS
BFS DFS
Breadth First Search Depth First Search
Visits vertices level by level Explores deeply before backtracking

Uses a queue Uses recursion or a stack
Uses an adjacency list in this practical Uses an adjacency matrix in this practical
Useful for finding shortest paths in unweighted
graphs

Useful for cycle detection and path
exploration

8. Applications
1. BFS: Finding the shortest route between two locations in an unweighted graph, social
network exploration and level-order traversal.
2. DFS: Maze solving, cycle detection, path exploration and topological sorting in directed
acyclic graphs.
9. Algorithm:
10. Flowchart:
11. Conclusion
the graph was represented using an adjacency matrix for DFS and an adjacency list for BFS.
Both traversals were performed successfully, starting from vertex A. BFS visited the vertices
level by level, whereas DFS explored a path deeply before backtracking.
'''
