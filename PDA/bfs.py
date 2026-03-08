from collections import deque

# BFS shortest path function
def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([start])
    parent = {start: None}

    visited.add(start)

    while queue:
        node = queue.popleft()

        if node == goal:
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)

    path.reverse()

    if path[0] == start:
        return path
    else:
        return None

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
source = 'A'
destination = 'F'

shortest_path = bfs_shortest_path(graph, source, destination)

if shortest_path:
    print("Shortest path:", " -> ".join(shortest_path))
else:
    print("No path exists")