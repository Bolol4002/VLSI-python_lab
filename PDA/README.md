# Graph Algorithms and Simulated Annealing - VLSI Design Applications (Beginner Guide)

This folder contains Python implementations of key graph algorithms used in **VLSI design**:
- **Search**: BFS/DFS (routing exploration), Dijkstra (shortest paths for wirelength).
- **Minimum Spanning Trees**: Kruskal/Prim (Steiner tree approximation for global routing).
- **Graph Partitioning**: Kernighan-Lin (KL), Simulated Annealing (min-cut for circuit placement, hypergraph models).

## Table of Contents
1. [BFS (`bfs.py`)](#1-bfs-py---breadth-first-search-shortest-path)
2. [DFS (`dfs.py`)](#2-dfs-py---depth-first-search-path)
3. [Dijkstra (`dijkstra.py`)](#3-dijkstra-py---shortest-path-with-edge-weights)
4. [Kruskal MST (`krushkal.py`)](#4-krushkalpy---kruskal-minimum-spanning-tree)
5. [Prim MST (`prims.py`)](#5-prims-py---prim-minimum-spanning-tree)
6. [Simulated Annealing Partition (`sa.py`)](#6-sa-py---simulated-annealing-graph-partition)
7. [Kernighan-Lin Partition (`kl_algorithm.py`)](#7-kl_algorithmpy---kernighan-lin-graph-bipartition)
8. [Quick Run Guide](#quick-run-guide)
9. [Algorithm Comparison](#algorithm-comparison)
10. [Python Basics](#python-basics-used-in-these-files-for-absolute-beginners)

Each file includes **line-by-line explanations** for beginners.

## Quick Run Guide
```bash
cd PDA
python bfs.py      # BFS path A->F
python dfs.py      # DFS path A->F
python dijkstra.py # Weighted shortest A->E
python krushkal.py # Kruskal MST edges
python prims.py    # Prim MST edges + total weight
python sa.py       # SA partition + min-cut
python kl_algorithm.py # KL partition + cut size
```

---

## 1) `bfs.py` - Breadth-First Search Shortest Path

### What this code does
Finds shortest path (fewest edges) from start to goal in unweighted graph.

### Line-by-line explanation
1. `from collections import deque`  
   Imports efficient queue for BFS level-order traversal.

*(Lines 2-40 unchanged from original - detailed path reconstruction using parent dict, sample graph A-F, output `A -> C -> F`)*

---

## 2) `dfs.py` - Depth-First Search Path

### What this code does
Finds **a** path (not necessarily shortest) using recursion/backtracking.

### Line-by-line explanation
1. `def dfs_path(graph, start, goal):`  
   Main function.

*(Lines 2-32 unchanged - recursive DFS helper, visited set, path list, sample output e.g. `A -> B -> E -> F`)*

---

## 3) `dijkstra.py` - Shortest Path with Edge Weights

### What this code does
Minimum distance path in weighted graph (non-negative weights).

### Line-by-line explanation
1. `import heapq`  
   Priority queue for greedy smallest-distance-first.

*(Lines 2-46 unchanged - distances dict, previous dict, pq loop, path recon, sample dist 11 path `['A', 'C', 'D', 'E']`)*

---

## 4) `krushkal.py` - Kruskal Minimum Spanning Tree

### What this code does
Connects all vertices with min total edge weight, no cycles.

### Line-by-line explanation
1. `def find(parent, i):`  
   Union-Find root finder with path compression.

2. `def union(parent, x, y):`  
   Merges sets by rank (simple).

*(Lines 3-43 unchanged - sort edges by weight, add if no cycle, 9-vertex example, outputs edges like `6 - 7 (weight 1)`)*

---

## 5) `prims.py` - Prim Minimum Spanning Tree

### What this code does
Greedy MST from adjacency **matrix** starting at vertex 0.

### Line-by-line explanation
1. `def prim(graph):`  
   Input: weight matrix.

*(Lines 2-45 unchanged - in_mst array, scan for min cross-edge, same 9x9 matrix as Kruskal, matching MST)*

---

## 6) `sa.py` - Simulated Annealing (Graph Partition)

### What this code does
Heuristic optimization: minimize edges crossing two partitions (min-cut). Probabilistic acceptance of worse moves.

### Status Update
**Fully runnable** - indentation fixed. Uses adjacency **list**.

### Line-by-line explanation
1-2. `import random`, `import math`  
   Random choices, exp() for Boltzmann prob.

3-10. `def calculate_cut_size(graph, partition):`  
   Count undirected crossing edges /2.

11-17. `def generate_neighbor(partition):`  
   Flip random node's partition (0<->1).

18-41. `def simulated_annealing(...)`:  
   Init random partition dict, loop cool T, accept delta<0 or exp(-delta/T), track best.

42-56. Sample graph (nodes 1-6), run, print `Node X -> Partition Y`, `Minimum Cut Size: Z` (varies ~2-4).

---

## 7) `kl_algorithm.py` - Kernighan-Lin Graph Bipartition

### What this code does
**Kernighan-Lin (KL) heuristic**: Start with even split A/B, try **all** pairwise swaps, keep first improving swap, repeat until no gain. Min-cut bipartition (VLSI placement: balance 2 chip regions).

**Note**: Naive O(V^4) - demo only (V=6). Real: O(V^2 log V) with priority queues.

### Line-by-line explanation
1-4. `def calculate_cut_size(graph, A, B):`  
   ```python
   cut_size = 0
   for i in A:
       for j in B:
           cut_size += graph[i][j]  # Matrix: 1=adj, 0=no edge
   return cut_size
   ```
   Brute-force cut (undirected assumed symmetric).

5-14. `def kl_partition(graph):`  
   ```python
   n = len(graph)  # e.g. 6
   A = list(range(n // 2))  # [0,1,2]
   B = list(range(n // 2, n))  # [3,4,5]
   print("Initial Partition:", A, B)
   initial_cut = calculate_cut_size(graph, A, B)
   print("Initial Cut Size:", initial_cut)  # e.g. 5
   ```
   Even initial split (0-based indices).

15-21. Nested loops **over all i in A, j in B**:
   ```python
   for i in range(len(A)):
       for j in range(len(B)):
           # Swap nodes
           A[i], B[j] = B[j], A[i]
           
           new_cut = calculate_cut_size(graph, A, B)
           if new_cut > initial_cut:  # Worse? Undo
               A[i], B[j] = B[j], A[i]
           else:  # Better/equal: keep, update baseline
               initial_cut = new_cut
   ```
   **Greedy swap**: Test every possible swap, keep first non-worsening, update cut.

22-25. `return A, B, initial_cut`  
   Final after all passes.

26-32. Sample **adj matrix** (6 nodes, symmetric 0/1):
   Row0: connected to 1,2 etc.
   Output example:
   ```
   Initial Partition: [0, 1, 2] [3, 4, 5]
   Initial Cut Size: 5
   Final Partition: [0, 3, 5] [1, 2, 4]
   Final Cut Size: 2
   ```

**VLSI Note**: Models netlist hypergraph as graph; partitions modules to left/right die area.

---

## Algorithm Comparison
| Algorithm | VLSI Use | Input | Complexity | Output |
|-----------|----------|--------|------------|--------|
| BFS/DFS | Routing search | Adj list | O(V+E) | Path |
| Dijkstra | Wirelength min | Weighted adj list | O((V+E)log V) | Dist + path |
| Kruskal | Steiner approx | Edge list | O(E log E) | MST edges |
| Prim | Steiner approx | Matrix/list | O(V^2) | MST edges + cost |
| SA | Placement partition | Adj list | Heuristic | Partition dict, cut |
| KL | Placement partition | Matrix | O(V^3) naive | Sets A/B, cut |

## Python Basics Used (for absolute beginners)
- `def`, `if/while/for`, lists/dicts/sets unchanged.
- **New**: `range(n)`, list slicing `range(n//2, n)`, tuple unpack swap `a,b = b,a`.
- **Matrix**: `graph[i][j]` 2D list access.

**Extend**: Add priorities to KL, FM 2-way partition, hMETIS wrapper for hypergraphs.

Happy learning VLSI graphs! 🚀

