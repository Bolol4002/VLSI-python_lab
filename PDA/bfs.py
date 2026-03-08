from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([start])
    parent = {start: None}  # parent[x] = node from which x was first reached

    while queue:
        node = queue.popleft()  # BFS explores level by level
        if node == goal:
            break

        for nxt in graph[node]:
            if nxt not in parent:  # not visited yet
                parent[nxt] = node
                queue.append(nxt)

    if goal not in parent:
        return None

    # Build path backwards: goal -> ... -> start, then reverse.
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

result = bfs_shortest_path(graph, "A", "F")
print("BFS shortest path:", " -> ".join(result) if result else "No path")