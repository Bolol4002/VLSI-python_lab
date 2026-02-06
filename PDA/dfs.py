# Function to find the shortest path using DFS
def dfs_shortest_path(graph, start, goal):
    shortest_path = None

    # Inner recursive DFS function
    def dfs(current, goal, visited, path):
        nonlocal shortest_path

        # Mark the current node as visited and add to path
        visited.add(current)
        path.append(current)

        # If goal is reached, check if this path is the shortest
        if current == goal:
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = list(path)
        else:
            # Visit all unvisited neighbors
            for neighbor in graph[current]:
                if neighbor not in visited:
                    dfs(neighbor, goal, visited, path)

        # Backtrack: remove current node from path and visited
        path.pop()
        visited.remove(current)

    # Start DFS from the source
    dfs(start, goal, set(), [])
    return shortest_path

# Graph representation as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

source = 'A'
destination = 'F'

# Find the shortest path using DFS
path = dfs_shortest_path(graph, source, destination)

if path:
    print("Path found (DFS):", " -> ".join(path))
else:
    print("No path exists")
