# Experiment No: 05
# Experiment Name:
# Write a Program to implement Depth First Search
# Source Code:

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

visited = set()

dfs(graph, 'A', visited)

# Output: A B D E C F