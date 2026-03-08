"""
dfs.py

Depth-First Search (DFS) based path-finding example.

This module shows a straightforward recursive DFS implementation that searches
for a path from `start` to `goal` in a directed or undirected graph represented
as an adjacency list.

Purpose and behavior:
- This implementation performs a full recursive depth-first traversal and keeps
  track of the current path. Whenever the `goal` node is reached the current
  path is compared to the best (shortest) path found so far and updated if
  shorter.
- The algorithm uses a `visited` set to prevent cycles within the current
  exploration path (so the same node will not appear twice in the same path).
  Importantly, because `visited` is modified on backtrack (a node is removed
  from `visited` when we backtrack), this implementation will allow different
  exploration branches to revisit nodes through different paths. In other
  words, it's exploring different simple paths (paths without repeated nodes).
- The implementation therefore tries to find a minimum-length path among all
  simple paths, but it does so by exhaustive search and is not optimized for
  shortest-path discovery. For shortest-path guarantees in unweighted graphs,
  BFS is the correct and efficient choice.

Recursion and backtracking:
- Recursion: The main work is done by a nested function `dfs(current, goal,
  visited, path)` which calls itself for each unvisited neighbor.
  Each recursive call descends one level in the search tree (one more node in
  the current path).
- Backtracking: After exploring all neighbors of a node, the function removes
  that node from `path` and `visited` before returning. This "undoes" the
  change the current call made and allows sibling branches of the recursion
  to explore alternative routes that include that node later.
- The combination of marking a node visited on entry and unmarking on exit
  is the standard pattern for exploring all simple paths without cycles.

Limitations and notes:
- Not guaranteed to be efficient for large graphs: worst-case time complexity is
  exponential in path length (it may examine many simple paths).
- Recursion depth: Python's recursion limit (usually ~1000) may be exceeded for
  very deep graphs. An iterative DFS (using an explicit stack) or increasing
  recursion limit may be necessary for deep graphs.
- For shortest path on an unweighted graph, BFS is both correct and more
  efficient. For weighted graphs, use Dijkstra's algorithm.
- This DFS implementation finds a shortest path by length only because it
  compares and keeps the shortest among all discovered simple paths; this is
  achieved by exploring all possibilities, not by DFS's nature.

Example usage is at the bottom of the file. To use these functions in other
modules, import `dfs_shortest_path`.
"""

from typing import Dict, List, Optional, Set


def dfs_shortest_path(
    graph: Dict[str, List[str]], start: str, goal: str
) -> Optional[List[str]]:
    """
    Find a path from `start` to `goal` using recursive DFS and return the
    shortest path found (in terms of number of nodes) among all simple paths.

    Parameters:
    - graph: adjacency list mapping node -> list of neighbors
    - start: source node
    - goal: destination node

    Returns:
    - A list of nodes representing the shortest path from start to goal, or
      None if no path exists.
    """
    shortest_path: Optional[List[str]] = None

    def dfs(current: str, goal_node: str, visited: Set[str], path: List[str]) -> None:
        """
        Recursive helper for DFS.

        Arguments:
        - current: node being visited now
        - goal_node: target node we want to reach
        - visited: set of nodes included in the current path (prevents cycles in the path)
        - path: list of nodes in the current path (in order)
        """
        nonlocal shortest_path

        # Mark the current node as part of the path and visited set.
        # This prevents revisiting it within the same path (avoids cycles).
        visited.add(current)
        path.append(current)

        # If we've reached the goal, evaluate whether this path is the best so far.
        if current == goal_node:
            # If we haven't found a path yet, or this one is shorter, replace it.
            if shortest_path is None or len(path) < len(shortest_path):
                # Make a copy to preserve the found path (path will change as we backtrack).
                shortest_path = list(path)
        else:
            # Explore neighbors depth-first.
            # Note: we copy the neighbor list iteration, but we do not copy visited/path;
            # those are shared and managed via backtracking.
            for neighbor in graph.get(current, []):
                # Only proceed if neighbor is not already in the current path.
                if neighbor not in visited:
                    dfs(neighbor, goal_node, visited, path)

        # Backtracking step:
        # Remove current node from path and visited so sibling branches can use it.
        # This is essential for exploring alternative simple paths that include `current`
        # at a different position in the path.
        path.pop()
        visited.remove(current)

    # Start DFS from start node.
    dfs(start, goal, set(), [])

    return shortest_path


# Example graph and invocation (kept as a simple script for demonstration):
if __name__ == "__main__":
    # Graph representation as an adjacency list (dictionary).
    # This example is directed in structure (neighbors listed only once),
    # but the same code works for undirected graphs if edges are present both ways.
    graph_example = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    source = "A"
    destination = "F"

    # Find a path using the DFS-based routine.
    path = dfs_shortest_path(graph_example, source, destination)

    if path:
        print("Path found (DFS):", " -> ".join(path))
    else:
        print("No path exists")
