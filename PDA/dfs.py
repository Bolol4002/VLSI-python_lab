def dfs_path(graph, start, goal):
    visited = set()
    path = []

    def dfs(node):
        visited.add(node)
        path.append(node)  # We are currently walking through this node.

        if node == goal:
            return True  # Goal found; keep the current path.

        for nxt in graph[node]:
            if nxt not in visited and dfs(nxt):
                return True  # Bubble success up the recursion stack.

        path.pop()  # Dead end, so remove this node from current path.
        return False

    return path if dfs(start) else None


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

result = dfs_path(graph, "A", "F")
print("DFS path:", " -> ".join(result) if result else "No path")