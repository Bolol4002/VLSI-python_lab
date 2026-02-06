from collections import deque

# Function to find the shortest path using BFS
def bfs_shortest_path(graph, start, goal):
    # Set to keep track of visited nodes
    visited = set()
    # Queue for BFS traversal
    queue = deque([start])
    # Dictionary to store parent of each node for path reconstruction
    parent = {start: None}

    visited.add(start)

    while queue:
        node = queue.popleft()

        # If goal is found, break
        if node == goal:
            break

        # Visit all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    # Reconstruct the path from goal to start
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)

    path.reverse()

    # If the path starts with the source, return it
    if path[0] == start:
        return path
    else:
        return None

# Graph representation as adjacency list
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

# Find the shortest path using BFS
shortest_path = bfs_shortest_path(graph, source, destination)

if shortest_path:
    print("Shortest path:", " -> ".join(shortest_path))
else:
    print("No path exists")
