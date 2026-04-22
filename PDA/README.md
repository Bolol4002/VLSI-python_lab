# PDA — Graph Algorithms for VLSI Design
## Complete Exam-Ready Reference Guide

This folder contains 7 Python implementations of classic graph algorithms applied to **Physical Design Automation (PDA)** in VLSI. Reading this guide alone should give you everything you need to understand the code, trace through examples by hand, and answer exam questions.

---

## Table of Contents

1. [BFS — Breadth-First Search (`bfs.py`)](#1-bfs--breadth-first-search-bfspy)
2. [DFS — Depth-First Search (`dfs.py`)](#2-dfs--depth-first-search-dfspy)
3. [Dijkstra — Weighted Shortest Path (`dijkstra.py`)](#3-dijkstra--weighted-shortest-path-dijkstrapy)
4. [Kruskal — Minimum Spanning Tree (`krushkal.py`)](#4-kruskal--minimum-spanning-tree-krushkalpy)
5. [Prim — Minimum Spanning Tree (`prims.py`)](#5-prim--minimum-spanning-tree-primspy)
6. [Kernighan-Lin — Graph Bipartition (`kl_algorithm.py`)](#6-kernighan-lin--graph-bipartition-kl_algorithmpy)
7. [Simulated Annealing — Graph Partition (`sa.py`)](#7-simulated-annealing--graph-partition-sapy)
8. [Algorithm Comparison Table](#algorithm-comparison-table)

---

## 1. BFS — Breadth-First Search (`bfs.py`)

### What is BFS?

Breadth-First Search explores a graph **level by level** — it visits all nodes at distance 1 from the source, then all nodes at distance 2, and so on. Because of this property, the first time BFS reaches a node it has taken the **shortest path** (fewest edges) to get there.

**VLSI Use:** Finding the shortest routing path between two pins in a chip floorplan where each connection hop has equal cost (e.g., grid-based maze routing).

---

### Functional Block Breakdown

#### Block 1 — Function Definition and Queue Initialisation
```python
from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([start])
    parent = {start: None}
```
- `deque` is a **double-ended queue** from Python's standard library. It supports O(1) appends and pops from both ends, making it ideal for BFS (we always append to the right and pop from the left).
- `queue` starts with only the `start` node inside it.
- `parent` is a dictionary that records **how each node was first discovered**. `parent[x] = y` means "we reached node x by coming from node y". The start node has `None` as its parent because it has no predecessor.
- This dictionary serves a dual purpose: it tracks **visited** nodes (any node in `parent` has been visited) and enables **path reconstruction** later.

#### Block 2 — BFS Main Loop
```python
    while queue:
        node = queue.popleft()
        if node == goal:
            break

        for nxt in graph[node]:
            if nxt not in parent:
                parent[nxt] = node
                queue.append(nxt)
```
- `queue.popleft()` removes and returns the **leftmost** (oldest) element — this is the FIFO behaviour that gives BFS its level-by-level property.
- If the popped node is the `goal`, we stop immediately. There is no need to keep exploring because BFS guarantees we already found the shortest path.
- For each neighbour `nxt` of the current node, we check `if nxt not in parent` — this is our visited check. If the neighbour hasn't been seen before, we record its parent and add it to the queue.
- We do **not** revisit nodes. The first time we reach a node is always via the shortest path.

#### Block 3 — Path Reconstruction
```python
    if goal not in parent:
        return None

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path
```
- If `goal` is not in `parent`, it was never reached — the graph is disconnected, so we return `None`.
- We reconstruct the path by **walking backwards** from the goal to the start using the `parent` dictionary. Starting from `goal`, we follow `parent[cur]` until we hit `None` (the start node's parent).
- `path.reverse()` flips the list so it reads from start → goal.

#### Block 4 — Sample Graph and Call
```python
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
```
- `graph` is a **dictionary of adjacency lists** (undirected graph). Each key is a node and its value is a list of directly connected neighbours.
- We search for the shortest path from `"A"` to `"F"`.

---

### Sample Input Explained

The graph looks like this:

```
    A
   / \
  B   C
 /|    \
D E     F
   \   /
    ---
```

Edges: A-B, A-C, B-D, B-E, C-F, E-F

There are two paths from A to F:
- A → B → E → F (3 hops)
- A → C → F (2 hops)

BFS will find A → C → F because it explores all 2-hop paths before any 3-hop path.

---

### Step-by-Step Execution Trace

| Step | Node Popped | Queue Before Pop | parent dict update |
|------|-------------|------------------|--------------------|
| 1 | A | [A] | B←A, C←A → queue=[B,C] |
| 2 | B | [B,C] | D←B, E←B → queue=[C,D,E] (A already in parent) |
| 3 | C | [C,D,E] | F←C → queue=[D,E,F] (A already in parent) |
| 4 | D | [D,E,F] | B already in parent; nothing added |
| 5 | E | [E,F] | B already in parent; F already in parent; nothing added |
| 6 | F | [F] | **F == goal → BREAK** |

**Path reconstruction:** F → (parent[F]=C) → (parent[C]=A) → (parent[A]=None) → stop
Reverse: **A → C → F**

### Output
```
BFS shortest path: A -> C -> F
```

---

## 2. DFS — Depth-First Search (`dfs.py`)

### What is DFS?

Depth-First Search dives as deep as possible down one branch before backtracking and trying other branches. It finds **a** path (not necessarily the shortest) using recursion and backtracking.

**VLSI Use:** Exploring all possible routing topologies, checking connectivity in netlists, cycle detection in dependency graphs.

---

### Functional Block Breakdown

#### Block 1 — Outer Function and State Variables
```python
def dfs_path(graph, start, goal):
    visited = set()
    path = []
```
- `visited` is a **set** — it stores nodes we have already explored so we don't get stuck in cycles. Set lookups are O(1).
- `path` is a **list** that records the current path being explored. It acts like a call stack trace.

#### Block 2 — Inner Recursive DFS Function
```python
    def dfs(node):
        visited.add(node)
        path.append(node)

        if node == goal:
            return True

        for nxt in graph[node]:
            if nxt not in visited and dfs(nxt):
                return True

        path.pop()
        return False
```
This is a **nested function** — it has access to `visited`, `path`, and `goal` from the outer scope.

- `visited.add(node)` — marks the current node as visited to prevent re-visiting.
- `path.append(node)` — adds the current node to the running path.
- `if node == goal: return True` — **base case**: we found the destination. The path list currently holds the complete solution, so we bubble `True` up the recursion chain without popping.
- `for nxt in graph[node]` — try each unvisited neighbour recursively.
- `if nxt not in visited and dfs(nxt): return True` — if the recursive call succeeds (returns True), we propagate the success upward immediately.
- `path.pop()` — **backtracking**: if we exhaust all neighbours without finding the goal, the current node is a dead end. We remove it from `path` before returning `False`.

#### Block 3 — Trigger and Return
```python
    return path if dfs(start) else None
```
- Calls `dfs(start)` to begin the search.
- Returns the completed `path` list if the goal was found, or `None` if not reachable.

#### Block 4 — Sample Graph and Call
```python
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
```
- Note: unlike the BFS graph, this graph is **directed** (B points to D and E, but D and E don't point back to B). D and F have no outgoing edges.

---

### Sample Input Explained

```
A → B → D (dead end)
        ↓
        E → F ✓
  ↓
  C → F ✓
```

DFS will go: A → B (first neighbour) → D (first neighbour of B, dead end) → backtrack to B → E → F (goal found).

It does NOT take the shorter A → C → F path because DFS doesn't care about shortest paths — it commits to the first branch it picks.

---

### Step-by-Step Execution Trace

```
dfs(A): visited={A}, path=[A]
  Try B (not visited):
    dfs(B): visited={A,B}, path=[A,B]
      Try D (not visited):
        dfs(D): visited={A,B,D}, path=[A,B,D]
          D != goal
          No unvisited neighbours (D's list is empty)
          path.pop() → path=[A,B]
          return False
      Try E (not visited):
        dfs(E): visited={A,B,D,E}, path=[A,B,E]
          E != goal
          Try F (not visited):
            dfs(F): visited={A,B,D,E,F}, path=[A,B,E,F]
              F == goal!
              return True  ← goal found, do NOT pop
          return True ← bubble up
        return True ← bubble up
      return True ← bubble up
    return True ← bubble up
```

### Output
```
DFS path: A -> B -> E -> F
```

---

## 3. Dijkstra — Weighted Shortest Path (`dijkstra.py`)

### What is Dijkstra's Algorithm?

Dijkstra's algorithm finds the **minimum-cost path** in a weighted graph (all edge weights must be non-negative). It greedily expands the node with the smallest known distance at each step, using a **min-heap** (priority queue) for efficiency.

**VLSI Use:** Finding the minimum wirelength path between two pins in a routing grid where different routing segments have different costs (e.g., congestion penalties, layer-change vias).

---

### Functional Block Breakdown

#### Block 1 — Initialisation
```python
import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    pq = [(0, start)]
```
- `heapq` is Python's **min-heap** library. The smallest element is always at index 0.
- `distances` — a dictionary initialised to infinity for every vertex. This represents "we don't know how to reach this node yet". The start node's distance is 0 because we're already there.
- `previous` — a dictionary for path reconstruction. `previous[x] = y` means "the best path to x came from y".
- `pq` — the **priority queue**, initialised with a tuple `(distance, node)`. Python's heapq always pops the smallest first, so nodes with smaller distances are processed first.

#### Block 2 — Main Greedy Loop
```python
    while pq:
        cur_dist, node = heapq.heappop(pq)
        if cur_dist > distances[node]:
            continue
        if node == end:
            break

        for nxt, weight in graph[node].items():
            new_dist = cur_dist + weight
            if new_dist < distances[nxt]:
                distances[nxt] = new_dist
                previous[nxt] = node
                heapq.heappush(pq, (new_dist, nxt))
```
- `heapq.heappop(pq)` — pops the node with the smallest distance.
- `if cur_dist > distances[node]: continue` — **stale entry check**. When we find a better path to a node, we push a new entry to the heap but don't remove the old one (heaps don't support efficient deletion). This check discards outdated entries.
- `if node == end: break` — once we pop the destination, we have its shortest distance (Dijkstra's guarantee).
- The inner loop **relaxes edges**: for each neighbour, if going through the current node is cheaper than the previously known distance, update `distances[nxt]`, record the predecessor, and push the new entry to the heap.

#### Block 3 — Path Reconstruction
```python
    if distances[end] == float("inf"):
        return float("inf"), None

    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = previous[cur]
    path.reverse()
    return distances[end], path
```
- If `distances[end]` is still infinity, the end node is unreachable.
- Walk backwards through `previous[]` from end to start, then reverse.

#### Block 4 — Sample Graph and Call
```python
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
```
- `graph` is a **dictionary of dictionaries** — `graph[u][v]` gives the weight of edge u→v.
- We find the shortest weighted path from A to E.

---

### Sample Input Explained

```
       4
  A -------> B
  |        ↗ |
2 |      1/  | 5
  ↓    /    ↓
  C <-----> D
  |    8    |
10|         | 2
  ↓         ↓
  E <--------
      (via D)
```

Key insight: the direct path A→C→E costs 2+10=12. But the path A→C→B→D→E costs 2+1+5+2=10.

---

### Step-by-Step Execution Trace

Initial: `distances = {A:0, B:∞, C:∞, D:∞, E:∞}`, `pq = [(0,A)]`

| Pop | cur_dist | Stale? | Neighbours relaxed | distances after | pq after |
|-----|----------|--------|--------------------|-----------------|----------|
| (0,A) | 0 | No | B: 0+4=4, C: 0+2=2 | B=4, C=2 | [(2,C),(4,B)] |
| (2,C) | 2 | No | A: 4>0 skip, **B: 2+1=3<4**, D: 2+8=10, E: 2+10=12 | B=3, D=10, E=12 | [(3,B),(4,B),(10,D),(12,E)] |
| (3,B) | 3 | No | A: 7>0 skip, C: 4>2 skip, **D: 3+5=8<10** | D=8 | [(4,B),(8,D),(10,D),(12,E)] |
| (4,B) | 4 | **YES** (dist[B]=3) | skip | unchanged | [(8,D),(10,D),(12,E)] |
| (8,D) | 8 | No | B: 13>3 skip, C: 16>2 skip, **E: 8+2=10<12** | E=10 | [(10,D),(10,E),(12,E)] |
| (10,D) | 10 | **YES** (dist[D]=8) | skip | unchanged | [(10,E),(12,E)] |
| (10,E) | 10 | No | **E == end → BREAK** | — | — |

**Path reconstruction:** E ← (previous[E]=D) ← (previous[D]=B) ← (previous[B]=C) ← (previous[C]=A) ← None
Reverse: **A → C → B → D → E**, total cost = **10**

### Output
```
Shortest distance: 10
Shortest path: A -> C -> B -> D -> E
```

---

## 4. Kruskal — Minimum Spanning Tree (`krushkal.py`)

### What is Kruskal's Algorithm?

A **Minimum Spanning Tree (MST)** connects all vertices in a graph with the minimum possible total edge weight, using exactly V−1 edges and no cycles. Kruskal's algorithm builds the MST by **sorting all edges by weight** and greedily adding the cheapest edge that doesn't create a cycle. Cycle detection is done efficiently using a **Union-Find** (Disjoint Set Union) data structure.

**VLSI Use:** Computing approximate Steiner trees for global routing — interconnecting a set of pins with minimum total wire length.

---

### Functional Block Breakdown

#### Block 1 — Union-Find: `find()` with Path Compression
```python
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]
```
- The Union-Find data structure represents a **forest of trees**, where each tree is a connected component.
- `parent[i]` stores the parent of node `i`. If `parent[i] == i`, then `i` is the **root** of its component.
- `find(parent, i)` returns the root of node `i`'s component — it tells you which "group" a node belongs to.
- **Path compression**: The line `parent[i] = find(parent, parent[i])` is the key optimisation. Instead of traversing the whole chain to the root, we directly attach node `i` to the root, flattening the tree for future queries.

#### Block 2 — Union-Find: `union()`
```python
def union(parent, x, y):
    rx = find(parent, x)
    ry = find(parent, y)
    if rx != ry:
        parent[ry] = rx
```
- Finds the roots of both nodes' components.
- If they are different, merges the two components by making one root point to the other (`parent[ry] = rx`).
- If `rx == ry`, they're already in the same component — adding this edge would create a cycle, so we skip it.

#### Block 3 — Kruskal's Main Logic
```python
def kruskal(vertices, edges):
    parent = list(range(vertices))
    mst = []

    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
            if len(mst) == vertices - 1:
                break
    return mst
```
- `parent = list(range(vertices))` — initially each node is its own root: `[0,1,2,3,4,5,6,7,8]`.
- `sorted(edges, key=lambda e: e[2])` — sorts all edges by their weight (index 2 of each tuple) in ascending order.
- For each edge in sorted order: if the two endpoints are in **different components** (no cycle), add the edge to MST and merge the components.
- Stop when `len(mst) == vertices - 1` — an MST has exactly V−1 edges.

#### Block 4 — Sample Input
```python
vertices = 9
edges = [
    (0,1,4), (0,7,8),
    (1,2,8), (1,7,11),
    (2,3,7), (2,8,2), (2,5,4),
    (3,4,9), (3,5,14),
    (4,5,10),
    (5,6,2),
    (6,7,1), (6,8,6),
    (7,8,7),
]
```
- 9 vertices (0 through 8), 14 edges.
- Edges are given as `(u, v, weight)` tuples.

---

### Sample Input Explained

The 9-node graph represents a network of circuit blocks or routing nodes. We want to connect all 9 nodes using the cheapest possible set of 8 edges (9−1=8).

---

### Step-by-Step Execution Trace

**Sorted edges:** (6,7,1), (2,8,2), (5,6,2), (0,1,4), (2,5,4), (6,8,6), (2,3,7), (7,8,7), (0,7,8), (1,2,8), (3,4,9), (4,5,10), (1,7,11), (3,5,14)

Initial parent: `[0, 1, 2, 3, 4, 5, 6, 7, 8]`

| Edge | weight | find(u) | find(v) | Cycle? | Action | MST count |
|------|--------|---------|---------|--------|--------|-----------|
| (6,7) | 1 | 6 | 7 | No | Add. parent[7]=6 | 1 |
| (2,8) | 2 | 2 | 8 | No | Add. parent[8]=2 | 2 |
| (5,6) | 2 | 5 | 6 | No | Add. parent[6]=5 → 7 also chains to 5 | 3 |
| (0,1) | 4 | 0 | 1 | No | Add. parent[1]=0 | 4 |
| (2,5) | 4 | 2 | 5 | No | Add. parent[5]=2 → all of {5,6,7,8} merge into 2's component | 5 |
| (6,8) | 6 | find(6)=**2** | find(8)=**2** | **YES** | Skip | 5 |
| (2,3) | 7 | 2 | 3 | No | Add. parent[3]=2 | 6 |
| (7,8) | 7 | find(7)=**2** | find(8)=**2** | **YES** | Skip | 6 |
| (0,7) | 8 | 0 | find(7)=**2** | No | Add. parent[2]=0 → {0,1} merges with {2,3,5,6,7,8} | 7 |
| (1,2) | 8 | find(1)=**0** | find(2)=**0** | **YES** | Skip | 7 |
| (3,4) | 9 | find(3)=**0** | 4 | No | Add. parent[4]=0 → all nodes connected | **8 → STOP** |

### Output
```
Edges in the Minimum Spanning Tree:
6 - 7 (weight 1)
2 - 8 (weight 2)
5 - 6 (weight 2)
0 - 1 (weight 4)
2 - 5 (weight 4)
2 - 3 (weight 7)
0 - 7 (weight 8)
3 - 4 (weight 9)
```
**Total MST weight = 1+2+2+4+4+7+8+9 = 37**

---

## 5. Prim — Minimum Spanning Tree (`prims.py`)

### What is Prim's Algorithm?

Prim's algorithm also builds the MST, but differently from Kruskal's. Instead of sorting all edges globally, it **grows the MST one vertex at a time** starting from a seed vertex. At each step, it picks the cheapest edge that connects a vertex already in the MST to a vertex not yet in the MST.

**VLSI Use:** Same as Kruskal — Steiner tree approximation for global routing. Prim is often preferred when the graph is given as an adjacency matrix (dense graphs).

---

### Functional Block Breakdown

#### Block 1 — Initialisation
```python
def prim(graph):
    n = len(graph)
    in_mst = [False] * n
    in_mst[0] = True

    mst_edges = []
    total = 0
```
- `n = len(graph)` — number of vertices (9 here).
- `in_mst` — a boolean array. `in_mst[i] = True` means vertex `i` has been added to the MST. We start from vertex 0.
- `mst_edges` — accumulates the chosen edges.
- `total` — running sum of the MST edge weights.

#### Block 2 — Outer Loop (Add One Vertex Per Iteration)
```python
    for _ in range(n - 1):
        best_u, best_v = -1, -1
        best_w = float("inf")
```
- We need exactly `n-1` edges for an MST, so we repeat `n-1` times.
- Each iteration, we search for the **minimum-weight crossing edge** (an edge from an in-MST vertex to a not-in-MST vertex).
- `best_w = float("inf")` resets the minimum tracker for each iteration.

#### Block 3 — Find Minimum Crossing Edge (Inner Double Loop)
```python
        for u in range(n):
            if in_mst[u]:
                for v in range(n):
                    w = graph[u][v]
                    if w != 0 and not in_mst[v] and w < best_w:
                        best_u, best_v, best_w = u, v, w
```
- Outer loop: scan all vertices `u` that are already in the MST.
- Inner loop: for each such `u`, examine all potential neighbours `v`.
- `graph[u][v]` is the adjacency matrix entry — 0 means no edge.
- Conditions: edge must exist (`w != 0`), `v` must not be in MST yet, and the weight must be better than the current best.

#### Block 4 — Extend the MST
```python
        in_mst[best_v] = True
        mst_edges.append((best_u, best_v, best_w))
        total += best_w

    return mst_edges, total
```
- Add the best vertex `best_v` to the MST.
- Record the edge and update the total weight.

#### Block 5 — Sample Graph (Adjacency Matrix)
```python
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],   # vertex 0
    [4, 0, 8, 0, 0, 0, 0,11, 0],   # vertex 1
    [0, 8, 0, 7, 0, 4, 0, 0, 2],   # vertex 2
    [0, 0, 7, 0, 9,14, 0, 0, 0],   # vertex 3
    [0, 0, 0, 9, 0,10, 0, 0, 0],   # vertex 4
    [0, 0, 4,14,10, 0, 2, 0, 0],   # vertex 5
    [0, 0, 0, 0, 0, 2, 0, 1, 6],   # vertex 6
    [8,11, 0, 0, 0, 0, 1, 0, 7],   # vertex 7
    [0, 0, 2, 0, 0, 0, 6, 7, 0],   # vertex 8
]
```
- This is the **same graph** as in Kruskal's, represented as a 9×9 matrix.
- `graph[u][v]` = weight of edge between u and v; 0 = no edge.
- The matrix is symmetric (undirected graph).

---

### Sample Input Explained

This is the **same 9-node network** as Kruskal's, just stored as a matrix instead of an edge list. The MST should be identical (total weight 37).

---

### Step-by-Step Execution Trace

Starting vertex = 0, `in_mst = [T,F,F,F,F,F,F,F,F]`

| Iteration | in_mst set | All crossing edges considered | Best edge chosen | Total |
|-----------|------------|-------------------------------|-----------------|-------|
| 1 | {0} | 0→1:4, 0→7:8 | **(0→1, w=4)** | 4 |
| 2 | {0,1} | 0→7:8, 1→2:8, 1→7:11 | **(0→7, w=8)** *(tie broken by order)* | 12 |
| 3 | {0,1,7} | 1→2:8, **7→6:1**, 7→8:7 | **(7→6, w=1)** | 13 |
| 4 | {0,1,6,7} | 1→2:8, **6→5:2**, 6→8:6, 7→8:7 | **(6→5, w=2)** | 15 |
| 5 | {0,1,5,6,7} | 1→2:8, **5→2:4**, 5→3:14, 5→4:10, 6→8:6, 7→8:7 | **(5→2, w=4)** | 19 |
| 6 | {0,1,2,5,6,7} | 2→3:7, **2→8:2**, 5→3:14, 5→4:10, 6→8:6, 7→8:7 | **(2→8, w=2)** | 21 |
| 7 | {0,1,2,5,6,7,8} | **2→3:7**, 5→3:14, 5→4:10 | **(2→3, w=7)** | 28 |
| 8 | {0,1,2,3,5,6,7,8} | **3→4:9**, 5→4:10 | **(3→4, w=9)** | **37** |

### Output
```
Edges in Prim MST:
0 - 1 (weight 4)
0 - 7 (weight 8)
7 - 6 (weight 1)
6 - 5 (weight 2)
5 - 2 (weight 4)
2 - 8 (weight 2)
2 - 3 (weight 7)
3 - 4 (weight 9)
Total weight: 37
```

> **Key insight:** Kruskal and Prim produce the **same total weight (37)** and the **same set of edges** — just discovered in a different order. This confirms both algorithms are correct MST algorithms.

> **Kruskal vs Prim:** Kruskal works edge-globally (sort all edges, use Union-Find). Prim works vertex-locally (grow one blob). Kruskal is better for sparse graphs (edge list). Prim with a matrix is O(V²), while Kruskal with Union-Find is O(E log E).

---

## 6. Kernighan-Lin — Graph Bipartition (`kl_algorithm.py`)

### What is the Kernighan-Lin Algorithm?

The Kernighan-Lin (KL) algorithm is a **heuristic** for **graph bipartitioning**: dividing the graph's vertices into two groups A and B of equal size such that the number of edges crossing between A and B (the **cut size**) is minimised.

It works by starting with an initial partition and iteratively trying all pairwise swaps (one node from A with one from B). It keeps any swap that does not worsen the cut size and discards swaps that do.

**VLSI Use:** Partitioning a circuit netlist into two halves for placement on a chip — e.g., assigning modules to the left vs. right side of the die to minimise inter-partition wire crossings.

---

### Functional Block Breakdown

#### Block 1 — Calculate Cut Size
```python
def calculate_cut_size(graph, A, B):
    cut_size = 0
    for i in A:
        for j in B:
            cut_size += graph[i][j]
    return cut_size
```
- Takes the adjacency matrix `graph` and the two partition lists `A` and `B`.
- Counts all edges between A and B by summing `graph[i][j]` for every pair (i∈A, j∈B).
- Since the matrix is symmetric (undirected graph), this counts each crossing edge exactly once (we iterate A×B, not all pairs).

#### Block 2 — Initial Partition Setup
```python
def kl_partition(graph):
    n = len(graph)
    A = list(range(n // 2))
    B = list(range(n // 2, n))

    print("Initial Partition:")
    print("A:", A)
    print("B:", B)
    initial_cut = calculate_cut_size(graph, A, B)
    print("Initial Cut Size:", initial_cut)
```
- `n = len(graph)` = 6 nodes.
- `A = [0, 1, 2]` (first half), `B = [3, 4, 5]` (second half) — a simple even split.
- Computes and prints the initial cut size before any swaps.

#### Block 3 — Greedy Swap Loop
```python
    for i in range(len(A)):
        for j in range(len(B)):
            A[i], B[j] = B[j], A[i]           # Try the swap

            new_cut = calculate_cut_size(graph, A, B)
            if new_cut > initial_cut:
                A[i], B[j] = B[j], A[i]       # Undo: swap is worse
            else:
                initial_cut = new_cut          # Keep: swap is better or equal

    return A, B, initial_cut
```
- Tries **all 9 possible swaps** (3 choices from A × 3 choices from B).
- For each swap: temporarily exchange `A[i]` and `B[j]`.
- Compute the new cut size.
- If the new cut is **worse** (strictly greater), undo the swap.
- If the new cut is **equal or better**, keep the swap and update the baseline cut size.
- This is a **greedy, single-pass** approach — not guaranteed to find the global optimum, but fast and often effective.

#### Block 4 — Sample Graph (Adjacency Matrix)
```python
graph = [
    [0, 1, 1, 0, 0, 0],   # node 0 connects to 1, 2
    [1, 0, 1, 1, 0, 0],   # node 1 connects to 0, 2, 3
    [1, 1, 0, 0, 1, 0],   # node 2 connects to 0, 1, 4
    [0, 1, 0, 0, 1, 1],   # node 3 connects to 1, 4, 5
    [0, 0, 1, 1, 0, 1],   # node 4 connects to 2, 3, 5
    [0, 0, 0, 1, 1, 0],   # node 5 connects to 3, 4
]
```

---

### Sample Input Explained

The 6-node graph has these edges: 0-1, 0-2, 1-2, 1-3, 2-4, 3-4, 3-5, 4-5.

Visually:
```
  0 --- 1 --- 3
  |   / |   / |
  |  /  |  /  |
  2 --- 4 --- 5
(A side)  (B side, initial)
```

Initial partition: A={0,1,2} (left side), B={3,4,5} (right side).

Crossing edges: **1→3** and **2→4** = **cut size = 2**.

---

### Step-by-Step Execution Trace

**Initial:** A=[0,1,2], B=[3,4,5], initial_cut=2

| i | j | A[i]↔B[j] | New A | New B | New cut | Decision |
|---|---|-----------|-------|-------|---------|----------|
| 0 | 0 | 0↔3 | [3,1,2] | [0,4,5] | 5 | **Undo** (5>2) |
| 0 | 1 | 0↔4 | [4,1,2] | [3,0,5] | 5 | **Undo** (5>2) |
| 0 | 2 | 0↔5 | [5,1,2] | [3,4,0] | 6 | **Undo** (6>2) |
| 1 | 0 | 1↔3 | [0,3,2] | [1,4,5] | 6 | **Undo** (6>2) |
| 1 | 1 | 1↔4 | [0,4,2] | [3,1,5] | 4 | **Undo** (4>2) |
| 1 | 2 | 1↔5 | [0,5,2] | [3,4,1] | 5 | **Undo** (5>2) |
| 2 | 0 | 2↔3 | [0,1,3] | [2,4,5] | 4 | **Undo** (4>2) |
| 2 | 1 | 2↔4 | [0,1,4] | [3,2,5] | 6 | **Undo** (6>2) |
| 2 | 2 | 2↔5 | [0,1,5] | [3,4,2] | 5 | **Undo** (5>2) |

Every swap makes the cut **worse** — the original partition is already a **local optimum** with cut size 2. KL correctly identifies it cannot improve further.

### Output
```
Initial Partition:
A: [0, 1, 2]
B: [3, 4, 5]
Initial Cut Size: 2

Final Partition:
Partition A: [0, 1, 2]
Partition B: [3, 4, 5]
Final Cut Size: 2
```

> **Exam note:** KL is a **local search** heuristic. It can get stuck at local optima. In this example, the algorithm started at the global optimum (cut=2), so no swaps helped. In practice with less ideal starting partitions, KL does improve the cut significantly. The real KL algorithm uses "gain" values (D-scores) for efficiency; this implementation is a simplified educational version.

---

## 7. Simulated Annealing — Graph Partition (`sa.py`)

### What is Simulated Annealing?

Simulated Annealing (SA) is a **probabilistic, metaheuristic optimisation** algorithm inspired by the process of slowly cooling molten metal (annealing) to reach a low-energy crystalline state.

Unlike KL which only accepts improvements, SA occasionally accepts **worse solutions** with a certain probability. This allows it to **escape local optima** and explore the solution space more broadly. As the "temperature" T decreases, the probability of accepting worse moves drops, and the algorithm converges to a solution.

**VLSI Use:** Circuit placement and floorplanning — minimising the cut size between partitions, or minimising wirelength/area in global placement. SA is widely used because it handles complex, non-convex cost landscapes.

---

### Functional Block Breakdown

#### Block 1 — Imports
```python
import random
import math
```
- `random` — for random initial partition, random node selection, and random acceptance check.
- `math` — for `math.exp()`, which computes the Boltzmann acceptance probability.

#### Block 2 — Cut Size Calculator
```python
def calculate_cut_size(graph, partition):
    cut_size = 0
    for u in graph:
        for v in graph[u]:
            if partition[u] != partition[v]:
                cut_size += 1
    return cut_size // 2
```
- `partition` is a dictionary: `partition[node]` = 0 or 1 (which group the node belongs to).
- For every edge (u, v), if `u` and `v` are in different partitions, it's a **crossing edge** — increment `cut_size`.
- Since the adjacency list is undirected, each edge (u,v) appears twice: once as u→v and once as v→u. Dividing by 2 corrects for this double-counting.

#### Block 3 — Neighbour Generator
```python
def generate_neighbor(partition):
    new_partition = partition.copy()
    node = random.choice(list(partition.keys()))
    new_partition[node] = 1 - new_partition[node]
    return new_partition
```
- Creates a **copy** of the current partition (we don't modify the original until we decide to accept).
- Picks a **random node** and **flips its group**: if it was in partition 0, it moves to 1, and vice versa.
- This is a minimal perturbation — a "neighbour" solution in the search space.
- Note: this can make the partition sizes unequal (SA doesn't enforce balanced partitions unless constrained).

#### Block 4 — Simulated Annealing Main Loop
```python
def simulated_annealing(graph, T=1000, cooling_rate=0.95, T_min=1):
    partition = {node: random.randint(0, 1) for node in graph}
    current_cost = calculate_cut_size(graph, partition)
    best_partition = partition.copy()
    best_cost = current_cost

    while T > T_min:
        new_partition = generate_neighbor(partition)
        new_cost = calculate_cut_size(graph, new_partition)
        delta = new_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / T):
            partition = new_partition
            current_cost = new_cost
        if current_cost < best_cost:
            best_cost = current_cost
            best_partition = partition.copy()
        T = T * cooling_rate

    return best_partition, best_cost
```

Let's break this down step by step:

- **`partition = {node: random.randint(0, 1) for node in graph}`** — randomly assigns each node to group 0 or 1. This is the random starting point.
- **`best_partition` / `best_cost`** — we track the **best solution ever seen**, not just the current one. The current partition may temporarily worsen, but `best_*` never does.
- **`while T > T_min:`** — the main annealing loop. We keep iterating as long as temperature is above the minimum threshold.
  - With T=1000, cooling_rate=0.95, T_min=1: the loop runs approximately **log(1/1000) / log(0.95) ≈ 135 iterations**.
- **`delta = new_cost - current_cost`** — the change in cost:
  - `delta < 0`: new solution is **better** — always accept.
  - `delta >= 0`: new solution is **worse** — accept with probability `e^(-delta/T)`.
- **Boltzmann acceptance probability `math.exp(-delta / T)`:**
  - At **high T**: `exp(-delta/T)` ≈ `exp(0)` = 1 — almost always accept (explore widely).
  - At **low T**: `exp(-delta/T)` → 0 — rarely accept worse solutions (exploit current good solution).
  - Example: delta=2, T=100 → prob = e^(-0.02) ≈ 0.98 (very likely to accept). delta=2, T=1 → prob = e^(-2) ≈ 0.135 (unlikely).
- **`T = T * cooling_rate`** — multiply by 0.95 each step (geometric cooling). Temperature decreases exponentially.

#### Block 5 — Sample Graph and Call
```python
graph = {
    1: [2, 3, 4],
    2: [1, 3, 5],
    3: [1, 2, 6],
    4: [1, 5],
    5: [2, 4, 6],
    6: [3, 5]
}
best_partition, min_cut = simulated_annealing(graph)
```
- Adjacency list representation (undirected). Nodes are integers 1–6.
- Edges: 1-2, 1-3, 1-4, 2-3, 2-5, 3-6, 4-5, 5-6.

---

### Sample Input Explained

```
    1 --- 2 --- 5
    |   / |     |
    |  /  |     |
    3 --- +     6
    |           |
    +-----------+
    (via 3-6 and 5-6)
```

Edges: 1-2, 1-3, 1-4, 2-3, 2-5, 3-6, 4-5, 5-6 (8 edges total).

The **theoretical minimum cut = 2**, achieved by isolating node 4 or node 6:
- Partition {4} vs {1,2,3,5,6}: cuts edges 1-4 and 4-5 → cut size = 2.
- Partition {6} vs {1,2,3,4,5}: cuts edges 3-6 and 5-6 → cut size = 2.

SA with T=1000 and slow cooling has ~135 iterations and a thorough exploration phase, so it frequently converges to the optimum cut of 2.

---

### Step-by-Step Concept Walkthrough (abbreviated)

```
Initial: e.g. partition = {1:0, 2:1, 3:0, 4:1, 5:0, 6:1}, cost = 5
T = 1000 (very high → almost any move accepted)

Iteration 1:
  Flip node 3: new partition = {1:0, 2:1, 3:1, 4:1, 5:0, 6:1}
  new_cost = 4, delta = -1 → ACCEPT (improvement)
  current_cost = 4, best_cost = 4

... (many iterations of exploration and exploitation) ...

T cooling: 1000 → 950 → 902.5 → ... → ~1 (after ~135 steps)

Near end (T ≈ 1, almost no bad moves accepted):
  Best found: e.g. {1:0, 2:0, 3:0, 4:0, 5:0, 6:1}, cost = 2
  Cuts: 3-6 and 5-6 only.
```

### Output (example — varies due to randomness)
```
Optimal Partition:
Node 1 -> Partition 0
Node 2 -> Partition 0
Node 3 -> Partition 0
Node 4 -> Partition 0
Node 5 -> Partition 0
Node 6 -> Partition 1
Minimum Cut Size: 2
```

> **Exam note:** SA output varies every run due to `random.randint` and `random.choice`. The minimum cut may be 2 (optimal), 3, or occasionally higher depending on the random seed. The key concepts to understand are: (1) random initial solution, (2) neighbourhood perturbation, (3) probabilistic acceptance via Boltzmann factor, (4) geometric temperature cooling, and (5) tracking the global best seen.

---

## Algorithm Comparison Table

| Algorithm | File | Problem Solved | Input Format | Time Complexity | Output |
|-----------|------|---------------|--------------|-----------------|--------|
| BFS | `bfs.py` | Shortest path (unweighted) | Adjacency list | O(V + E) | Path list |
| DFS | `dfs.py` | Any path (unweighted) | Adjacency list | O(V + E) | Path list |
| Dijkstra | `dijkstra.py` | Shortest path (weighted) | Weighted adj. list | O((V+E) log V) | Distance + path |
| Kruskal | `krushkal.py` | Minimum Spanning Tree | Edge list | O(E log E) | MST edge list |
| Prim | `prims.py` | Minimum Spanning Tree | Adjacency matrix | O(V²) | MST edges + total |
| KL | `kl_algorithm.py` | Graph bipartition (min-cut) | Adjacency matrix | O(V³) naive | Two sets A, B + cut |
| Sim. Annealing | `sa.py` | Graph partition (min-cut) | Adjacency list | Heuristic (~O(iter)) | Partition dict + cut |

---

## Key Concepts for the Exam

### Data Structures Used
| Structure | Used In | Why |
|-----------|---------|-----|
| `deque` | BFS | O(1) popleft for FIFO queue |
| `set` | DFS | O(1) visited lookup |
| `heapq` (min-heap) | Dijkstra | Always process cheapest node first |
| Union-Find (parent array) | Kruskal | Detect cycles in O(α(V)) ≈ O(1) |
| Boolean array `in_mst` | Prim | O(1) membership check |
| Dict `partition[node]` | SA, KL | Map each node to its group (0 or 1) |

### Cut Size in Graph Partitioning
The **cut size** is the number of edges with one endpoint in group A and the other in group B. Minimising cut size means fewer inter-partition connections — in VLSI this means fewer long wires crossing between chip regions.

### BFS vs DFS
- **BFS** guarantees the **shortest path** (fewest hops) because it explores level by level.
- **DFS** finds **a** path, not necessarily shortest. It's useful for full graph exploration and cycle detection.
- Both are O(V+E) but BFS uses more memory (queue stores an entire level), DFS uses O(depth) stack memory.

### Kruskal vs Prim
- Both produce the **same MST** (same edges, same total weight).
- **Kruskal**: sort all edges globally, use Union-Find to avoid cycles. Better for **sparse** graphs.
- **Prim**: grow one blob from a seed vertex, scan for minimum crossing edge. Better for **dense** graphs (matrix representation).

### Simulated Annealing vs Kernighan-Lin
- **KL**: deterministic, fast, but can get stuck at local optima.
- **SA**: probabilistic, slower, but can escape local optima due to the random acceptance of worse moves.
- SA is generally more powerful for complex partitioning problems, while KL is used as a post-processing refinement step.

---

*Happy studying! Master these 7 algorithms and you'll have a solid foundation in graph-based physical design automation.* 🚀pped | Action | Queue after |
|------|--------|--------|-------------|
| 1 | A | Enqueue B