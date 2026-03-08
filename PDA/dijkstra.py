import heapq
from typing import Any, Dict, List, Tuple

# Dijkstra's algorithm to find the shortest path between `start` and `end`
# in a weighted graph with non-negative edge weights.
#
# Key ideas to understand in this implementation:
# 1. Distances dictionary:
#    - We maintain a mapping `distances[vertex]` which holds the currently
#      known shortest distance from `start` to `vertex`. It is initialized
#      to infinity for all vertices except `start` which is 0.
#
# 2. Priority queue (min-heap):
#    - We use a min-heap (Python's `heapq`) to always extract the vertex
#      with the smallest known tentative distance. Each heap entry is a
#      tuple `(distance, vertex)`.
#    - The heap acts as the frontier of vertices to explore next. Using a
#      heap ensures we always expand the most promising vertex first,
#      which is what gives Dijkstra its efficiency and correctness.
#
# 3. Relaxation step:
#    - For each neighbor of the current vertex, we compute a candidate
#      distance: `current_distance + edge_weight`.
#    - If this candidate distance is smaller than the currently stored
#      `distances[neighbor]`, we have found a shorter path to `neighbor`.
#      We then update `distances[neighbor]`, record the predecessor for
#      path reconstruction, and push the new candidate onto the heap.
#    - Pushing to the heap does not remove the old (larger) distance entry
#      for that neighbor. When that stale entry is later popped, we detect
#      it (because its distance is greater than the stored `distances[vertex]`)
#      and skip processing it. This lazy deletion keeps the implementation
#      simple and correct.
#
# 4. Early exit:
#    - Once we pop the destination `end` from the heap, its stored distance
#      is guaranteed to be the final shortest distance (because the heap
#      always yields the smallest tentative distance). We can break early
#      in that case for a small optimization.
#
# 5. Path reconstruction:
#    - We store a `previous` mapping so that once the algorithm finishes
#      (or reaches `end`), we can walk backwards from `end` to `start` to
#      reconstruct the shortest path.
#
# Complexity:
# - For a graph with V vertices and E edges, using a binary heap:
#   O((V + E) log V) which is commonly simplified to O(E log V) for sparse graphs.


def dijkstra(
    graph: Dict[Any, Dict[Any, float]], start: Any, end: Any
) -> Tuple[float, List[Any]]:
    """
    Find the shortest path and its distance from `start` to `end` in `graph`.

    Parameters:
    - graph: adjacency mapping where graph[u] is a dict of {v: weight}.
             Example: { 'A': {'B': 4, 'C': 2}, 'B': {'A':4, 'C':1, 'D':5}, ... }
    - start: source vertex
    - end: destination vertex

    Returns:
    - (distance, path) where distance is the shortest distance (float('inf') if unreachable)
      and path is a list of vertices from start to end (empty list if unreachable).
    """
    # Initialize distances: set every vertex distance to infinity except start.
    distances: Dict[Any, float] = {vertex: float("inf") for vertex in graph}
    distances[start] = 0.0

    # For reconstructing the path: previous[v] = u means the best known path to v
    # goes through u.
    previous: Dict[Any, Any] = {vertex: None for vertex in graph}

    # The priority queue stores tuples of (distance_so_far, vertex). We start with the start node.
    # The heap always pops the vertex with the smallest tentative distance.
    priority_queue: List[Tuple[float, Any]] = [(0.0, start)]

    # Main loop: keep processing the closest tentative vertex until heap is empty
    # or we reach the destination.
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If we pop a vertex whose distance in the heap is greater than the currently
        # known shortest distance, this is a stale entry (from a previous relaxation).
        # Skip it. This is the "lazy deletion" approach for the priority queue.
        if current_distance > distances[current_vertex]:
            # This entry is outdated because a shorter path to current_vertex
            # has already been found and pushed onto the heap.
            continue

        # Early exit optimization: if we've popped the destination, its distance is final.
        if current_vertex == end:
            break

        # Iterate over neighbors and perform relaxation.
        # Relaxation: if going from start -> ... -> current_vertex -> neighbor gives a
        # shorter path than the currently known path to neighbor, update it.
        for neighbor, weight in graph[current_vertex].items():
            # Compute distance to neighbor via current_vertex
            candidate_distance = current_distance + weight

            # If the candidate distance is better, update distance and previous,
            # and push the new state to the heap.
            if candidate_distance < distances[neighbor]:
                distances[neighbor] = candidate_distance
                previous[neighbor] = current_vertex
                # Push the updated tentative distance for neighbor. If there was a previous
                # longer tentative distance for neighbor already in the heap, it will remain
                # until popped and then skipped due to the check above.
                heapq.heappush(priority_queue, (candidate_distance, neighbor))

    # After the algorithm, reconstruct the path from end back to start.
    if distances[end] == float("inf"):
        # Destination is unreachable from start.
        return float("inf"), []

    path: List[Any] = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()  # reverse the path to go from start -> ... -> end

    return distances[end], path


# Example usage:
if __name__ == "__main__":
    # Graph represented as adjacency dict with non-negative weights
    graph_example = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2},
        "E": {"C": 10, "D": 2},
    }
    source = "A"
    destination = "E"

    shortest_distance, shortest_path = dijkstra(graph_example, source, destination)

    if shortest_path:
        print("Shortest distance:", shortest_distance)
        print("Shortest path:", " -> ".join(shortest_path))
    else:
        print("No path exists from", source, "to", destination)
