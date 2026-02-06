import heapq

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(graph, start, end):
    # Initialize distances to all vertices as infinity
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    # Dictionary to store the previous node in optimal path
    previous = {vertex: None for vertex in graph}
    # Priority queue to select the edge with the smallest weight
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        # If the destination is reached, break
        if current_vertex == end:
            break
        # If a shorter path to current_vertex has already been found, skip
        if current_distance > distances[current_vertex]:
            continue
        # Visit all neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # If a shorter path to neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    # Reconstruct the shortest path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return distances[end], path

# Graph representation as adjacency list with weights
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}
source = 'A'
destination = 'E'

# Find the shortest distance and path using Dijkstra's algorithm
shortest_distance, shortest_path = dijkstra(graph, source, destination)
print("Shortest distance:", shortest_distance)
print("Shortest path:", " -> ".join(shortest_path))
