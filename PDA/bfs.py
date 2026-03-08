"""
BFS (Breadth-First Search) shortest-path implementation with improved comments.

This module finds the shortest path between two nodes in an unweighted graph using BFS.
BFS explores the graph in "layers" (distance from the start node), so the first time
the goal node is reached the path found is guaranteed to be one of the shortest (in
terms of number of edges) from the start to the goal.

Key data structures:
- `queue` (collections.deque): FIFO structure used to process nodes in level order.
- `visited` (set): tracks nodes we've already enqueued/processed so we don't revisit them.
- `parent` (dict): maps each visited node to the node from which it was first discovered.
  This is used to reconstruct the actual path from `start` to `goal` after the search.

Time complexity: O(V + E) where V is vertices and E is edges (each node and edge is
processed a bounded number of times).
"""

from collections import deque
from typing import Dict, Hashable, List, Optional


def bfs_shortest_path(
    graph: Dict[Hashable, List[Hashable]], start: Hashable, goal: Hashable
) -> Optional[List[Hashable]]:
    """
    Find the shortest path (fewest edges) between `start` and `goal` in an
    unweighted graph represented as an adjacency list.

    Parameters:
    - graph: mapping from node -> list of neighbor nodes
    - start: starting node
    - goal: destination node

    Returns:
    - A list of nodes representing the path from `start` to `goal` (inclusive),
      e.g. [start, ..., goal], or `None` if no path exists.
    """

    # Quick validation and trivial case
    if start not in graph or goal not in graph:
        # If either endpoint is not in the graph there can be no path.
        return None
    if start == goal:
        # Start equals goal: shortest path is the single-node path.
        return [start]

    # `visited` prevents re-enqueueing the same node multiple times which would
    # otherwise cause infinite loops on cyclic graphs and degrade performance.
    visited = set()
    visited.add(start)

    # `parent` stores the predecessor of each discovered node in the BFS tree.
    # When we discover a neighbor `n` from node `u`, we set parent[n] = u.
    # After reaching the goal we can walk the parent links back to reconstruct
    # the full path.
    parent: Dict[Hashable, Optional[Hashable]] = {start: None}

    # BFS uses a queue (FIFO). Initialize with the starting node.
    queue = deque([start])

    # Standard BFS loop: process nodes in FIFO order so nodes are explored by
    # increasing distance (number of edges) from `start`.
    while queue:
        node = queue.popleft()

        # If we reached the goal, we can stop searching. Because BFS expands
        # nodes by increasing distance, the first time we encounter `goal`
        # yields a shortest path.
        if node == goal:
            break

        # Explore all neighbors of the current node.
        # For each neighbor not yet visited, mark it visited, record its parent,
        # and enqueue it so its neighbors will be explored later.
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    # If the goal was never discovered, it won't be in `parent`.
    if goal not in parent:
        return None

    # Reconstruct the path by walking predecessors from `goal` back to `start`.
    path: List[Hashable] = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)

    # `path` is built from goal -> start, so reverse it to get start -> goal.
    path.reverse()
    return path


# Example usage guarded by __main__ so importing this module doesn't run demo code.
if __name__ == "__main__":
    # Example graph (undirected) represented as an adjacency list.
    # Note: for an undirected graph each edge appears in both endpoints' lists.
    graph_example = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    source = "A"
    destination = "F"

    shortest_path = bfs_shortest_path(graph_example, source, destination)

    if shortest_path:
        print("Shortest path:", " -> ".join(shortest_path))
    else:
        print("No path exists")
