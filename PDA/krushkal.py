"""
krushkal.py

Kruskal's algorithm implementation with a well-documented union-find data structure.

This module shows:
- How edges are sorted by weight.
- How a union-find (disjoint set) data structure is used to detect cycles
  and to efficiently decide whether adding an edge will connect two
  different components.
- How the Minimum Spanning Tree (MST) is assembled.

Key concepts explained inline:
- Union-Find operations:
    * `find(x)` returns the set representative (root) for element `x`.
      This implementation uses path compression to flatten the structure,
      giving amortized nearly-constant time per operation.
    * `union(x, y)` attaches one tree to another using union by rank
      (approximate tree height) so that the resulting tree remains shallow.

- Kruskal algorithm steps:
    1. Sort all edges in non-decreasing order by weight.
    2. Iterate edges in that order; for each edge (u, v, w):
       - If `u` and `v` are in different sets, include the edge in MST and
         union their sets.
       - Otherwise, skip the edge (it would form a cycle).
    3. Stop when MST contains (V - 1) edges or when edges are exhausted.

Complexity:
- Sorting edges: O(E log E)
- Union-find operations: near O(α(V)) per operation (inverse Ackermann)
- Overall: O(E log E) dominated by sorting (E = number of edges).

This file is intended to replace the original, minimally commented version
with clear explanations at each logical block so you can follow the algorithm.
"""

from typing import List, Tuple

# Type aliases for readability:
Edge = Tuple[int, int, int]  # (u, v, weight)


class UnionFind:
    """
    Disjoint set (union-find) data structure with path compression and union by rank.

    Attributes:
        parent: parent[i] is the parent of node `i`. If parent[i] == i, `i` is a root.
        rank:  rank[i] is an upper-bound estimate of the height of the tree rooted at `i`.
    """

    def __init__(self, size: int):
        """
        Initialize `size` disjoint sets: each element is its own parent (root).

        Args:
            size: number of elements (typically equal to number of vertices).
        """
        # Initially each node is in its own set (parent to itself).
        self.parent = [i for i in range(size)]
        # Rank starts at 0 for all nodes.
        self.rank = [0] * size

    def find(self, x: int) -> int:
        """
        Find the representative (root) of the set that `x` belongs to.

        Uses path compression: after the operation, `x` (and all nodes on the path)
        point directly to the root. This keeps future `find` operations fast.

        Args:
            x: element index

        Returns:
            root representative of the set containing `x`
        """
        # If x is its own parent, it's the root.
        if self.parent[x] != x:
            # Recursively find root and compress the path.
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union the sets containing `x` and `y`.

        Uses union by rank: attach the smaller rank tree under the higher rank root.
        If both ranks are equal, pick one root arbitrarily and increment its rank.

        Args:
            x: element index
            y: element index

        Returns:
            True if a union was performed (the two elements were previously in different sets),
            False if they were already in the same set.
        """
        xroot = self.find(x)
        yroot = self.find(y)

        # If both have the same root, they are already connected -> no union.
        if xroot == yroot:
            return False

        # Union by rank: attach smaller rank tree under larger rank tree.
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            # Arbitrarily make xroot the parent, and increase its rank.
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

        return True


def kruskal(vertices: int, edges: List[Edge]) -> Tuple[List[Edge], int]:
    """
    Compute the Minimum Spanning Tree (MST) using Kruskal's algorithm.

    Args:
        vertices: number of vertices in the graph (assumed vertices are 0..vertices-1)
        edges: list of edges as tuples (u, v, weight)

    Returns:
        A tuple (mst_edges, total_weight) where:
            - mst_edges: list of edges included in the MST (in the order chosen)
            - total_weight: sum of weights of the MST edges
    """
    # 1) Sort edges by weight (non-decreasing). Stable sort is fine.
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    # 2) Prepare union-find to detect cycles and manage components
    uf = UnionFind(vertices)

    mst: List[Edge] = []
    total_weight = 0

    # 3) Iterate through sorted edges and add to MST if they connect different components.
    for u, v, w in sorted_edges:
        # Debug comment:
        # For each edge, we check whether its endpoints belong to different sets.
        # If they do, adding the edge won't form a cycle and we include it in the MST.
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            total_weight += w
            # Stop early if we already have V-1 edges (spanning tree complete)
            if len(mst) == vertices - 1:
                break

    # Return the collected MST edges and their total cost.
    return mst, total_weight


if __name__ == "__main__":
    # Example usage with a small graph (same as traditional textbook examples).
    #
    # Vertex indices: 0 .. 8
    # Edge format: (u, v, weight)
    edges_example: List[Edge] = [
        (0, 1, 4),
        (0, 7, 8),
        (1, 2, 8),
        (1, 7, 11),
        (2, 3, 7),
        (2, 8, 2),
        (2, 5, 4),
        (3, 4, 9),
        (3, 5, 14),
        (4, 5, 10),
        (5, 6, 2),
        (6, 7, 1),
        (6, 8, 6),
        (7, 8, 7),
    ]
    num_vertices = 9

    # Run Kruskal's algorithm and print the result.
    mst_edges, mst_weight = kruskal(num_vertices, edges_example)

    print("Edges in the Minimum Spanning Tree (u, v, weight):")
    for edge in mst_edges:
        print(edge)
    print("Total weight of MST:", mst_weight)

    # Notes for further exploration:
    # - If the graph is disconnected, Kruskal will produce a minimum spanning forest:
    #   a MST for each connected component. The number of edges returned will be
    #   less than (V - 1) in that case.
    # - You can adapt this implementation to work with arbitrary vertex labels by
    #   mapping labels to 0..n-1 indices before calling `kruskal`.
