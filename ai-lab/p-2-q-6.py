# Experiment No: 06
# Experiment Name:
# Write a program to implement Breadth First search
# Source Code:

# Cell 1:
from collections import deque

# Cell 2:
def bfs(graph, start):
    vis = set()
    que = deque()

    vis.add(start)
    que.append(start)

    while que:
        n = que.popleft()
        print(n, end=" ")

        for i in graph[n]:
            if i not in vis:
                vis.add(i)
                que.append(i)

# Cell 3:
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"],
}
# Cell 4:
bfs(graph, "A")

# Output: A B C D E F