#!/usr/bin/env python3
"""
Prim's algorithm implementation with explanatory comments.

This module finds the Minimum Spanning Tree (MST) of a connected, undirected,
weighted graph represented as an adjacency matrix.

Key data structures:
- graph: adjacency matrix (list of lists). graph[i][j] is the weight of the
  edge between vertex i and vertex j. A value of 0 indicates no direct edge.
- selected: boolean list indicating whether a vertex is already included in
  the growing MST.
- The algorithm repeatedly selects the smallest-weight edge that connects any
  vertex already in the MST to any vertex not yet in the MST.

Time complexity: O(V^2) for the adjacency-matrix implementation, where V is
the number of vertices.
"""

import sys
from typing import List, Tuple


def prim(graph: List[List[int]], vertices: int) -> List[Tuple[int, int, int]]:
    """
    Compute the Minimum Spanning Tree (MST) using Prim's algorithm.

    Parameters:
    - graph: adjacency matrix of size V x V where graph[i][j] is the weight of
      edge i-j (0 means no edge).
    - vertices: number of vertices (V). It should equal len(graph).

    Returns:
    - mst_edges: list of edges included in the MST as tuples (u, v, weight).
      The function also prints the selected edges and their weights.
    """
    # 'selected' keeps track of which vertices are already included in the MST.
    # Initially, no vertex is selected except we pick vertex 0 as the starting point.
    selected = [False] * vertices
    selected[0] = True  # start from vertex 0 (arbitrary choice)

    # We'll collect the MST edges here to return them to the caller.
    mst_edges: List[Tuple[int, int, int]] = []

    # Print a human-friendly header showing what will be printed below.
    print("Edge \tWeight")

    # We need to add exactly (V - 1) edges to connect V vertices in a tree.
    for _ in range(vertices - 1):
        # 'minimum' stores the current best (smallest) edge weight found in the search.
        # We initialize it to a very large value so the first valid edge replaces it.
        minimum = sys.maxsize

        # x and y will store the vertices (u, v) corresponding to the minimum edge.
        # x is in the set of already selected vertices, y is in the set of unselected vertices.
        x = -1
        y = -1

        # Search for the minimum-weight edge that crosses from the selected set to the
        # unselected set. We consider all edges (i, j) where 'i' is selected and
        # 'j' is not selected and graph[i][j] != 0 (i.e., an edge exists).
        for i in range(vertices):
            # If vertex i has been included in the MST already, examine its edges.
            if selected[i]:
                for j in range(vertices):
                    # Consider only edges to unselected vertices and where an edge exists.
                    if (not selected[j]) and graph[i][j] != 0:
                        # If this edge has smaller weight than the best so far, remember it.
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        # At this point, (x, y, minimum) is the smallest edge that expands the MST.
        # Record and output this edge. Mark the new vertex y as selected so it becomes
        # part of the MST for the next iteration.
        if x != -1 and y != -1:
            print(f"{x} - {y} \t{graph[x][y]}")
            mst_edges.append((x, y, graph[x][y]))
            selected[y] = True
        else:
            # If we could not find an edge to add, the graph may be disconnected.
            # In that case, Prim's algorithm cannot produce a spanning tree covering
            # all vertices.
            raise ValueError(
                "Graph is disconnected; MST cannot be formed for all vertices."
            )

    return mst_edges


if __name__ == "__main__":
    # Example graph as an adjacency matrix. A 0 entry means "no direct edge" between vertices.
    # The example below is the same 9-vertex graph used in many textbook examples.
    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0],
    ]

    # Run Prim's algorithm and capture the resulting MST edges.
    mst = prim(graph, 9)

    # Optional: compute total weight of the MST and display it.
    total_weight = sum(weight for (_, _, weight) in mst)
    print("\nTotal weight of MST:", total_weight)
