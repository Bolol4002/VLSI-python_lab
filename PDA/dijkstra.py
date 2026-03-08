import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    pq = [(0, start)]  # (distance, node)

    while pq:
        cur_dist, node = heapq.heappop(pq)
        if cur_dist > distances[node]:
            continue  # Outdated heap entry.
        if node == end:
            break

        for nxt, weight in graph[node].items():
            new_dist = cur_dist + weight
            if new_dist < distances[nxt]:
                distances[nxt] = new_dist
                previous[nxt] = node
                heapq.heappush(pq, (new_dist, nxt))

    if distances[end] == float("inf"):
        return float("inf"), None

    # Follow previous[] from end to start, then reverse.
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = previous[cur]
    path.reverse()
    return distances[end], path

graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2},
    "E": {"C": 10, "D": 2},
}

dist, path = dijkstra(graph, "A", "E")

print("Shortest distance:", dist)
print("Shortest path:", " -> ".join(path) if path else "No path")