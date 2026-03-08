def dfs_shortest_path(graph, start, goal):
    shortest_path = None

    def dfs(current, goal, visited, path):
        nonlocal shortest_path

        visited.add(current)
        path.append(current)

        if current == goal:
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = list(path)
        else:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    dfs(neighbor, goal, visited, path)

        path.pop()
        visited.remove(current)

    dfs(start, goal, set(), [])
    return shortest_path

# Graph representation
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

path = dfs_shortest_path(graph, source, destination)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path exists")