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

'''