# Graph Algorithms and Simulated Annealing - Beginner Friendly Guide

This folder contains Python programs for:
- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- Dijkstra shortest path
- Kruskal Minimum Spanning Tree
- Prim Minimum Spanning Tree
- Simulated Annealing (for graph partition / min-cut style objective)

This README explains each file **line by line** in simple language.

---

## 1) `bfs.py` - Breadth-First Search Shortest Path

### What this code does
It finds a shortest path (in number of edges) from one node to another in an unweighted graph.

### Line-by-line explanation
1. `from collections import deque`
   - Imports `deque`, a fast queue structure from Python's standard library.
   - BFS needs a queue (First-In, First-Out).

2. (blank line)
   - Blank lines improve readability.

3. `def bfs_shortest_path(graph, start, goal):`
   - Defines a function named `bfs_shortest_path`.
   - Inputs:
     - `graph`: connection map (adjacency list)
     - `start`: starting node
     - `goal`: destination node

4. `    queue = deque([start])`
   - Creates a queue and puts `start` inside it.

5. `    parent = {start: None}  # parent[x] = node from which x was first reached`
   - Creates a dictionary called `parent`.
   - It stores from which node each node was discovered.
   - `start` has no parent, so value is `None`.

6. (blank line)

7. `    while queue:`
   - Loop while queue is not empty.

8. `        node = queue.popleft()  # BFS explores level by level`
   - Removes the leftmost item from queue.
   - This is the current node being processed.

9. `        if node == goal:`
   - If current node is the destination...

10. `            break`
    - Stop search early.

11. (blank line)

12. `        for nxt in graph[node]:`
    - Check every neighbor (`nxt`) of current node.

13. `            if nxt not in parent:  # not visited yet`
    - If neighbor has never been discovered before...

14. `                parent[nxt] = node`
    - Save how we reached this neighbor.

15. `                queue.append(nxt)`
    - Add neighbor to queue for later processing.

16. (blank line)

17. `    if goal not in parent:`
    - After BFS, if goal was never discovered...

18. `        return None`
    - Return `None` meaning no path exists.

19. (blank line)

20. `    # Build path backwards: goal -> ... -> start, then reverse.`
    - Comment: explains path reconstruction idea.

21. `    path = []`
    - Empty list to store the path.

22. `    cur = goal`
    - Start from destination and walk backward.

23. `    while cur is not None:`
    - Continue until reaching the start's parent (`None`).

24. `        path.append(cur)`
    - Add current node to path list.

25. `        cur = parent[cur]`
    - Move to parent of current node.

26. `    path.reverse()`
    - Reverse list to get start -> goal order.

27. `    return path`
    - Return final path list.

28. (blank line)

29. (blank line)

30. `graph = {`
    - Defines sample graph as dictionary.

31. `    "A": ["B", "C"],`
    - Node `A` connects to `B` and `C`.

32. `    "B": ["A", "D", "E"],`
    - Node `B` connects to `A`, `D`, `E`.

33. `    "C": ["A", "F"],`
    - Node `C` connects to `A`, `F`.

34. `    "D": ["B"],`
    - Node `D` connects to `B`.

35. `    "E": ["B", "F"],`
    - Node `E` connects to `B`, `F`.

36. `    "F": ["C", "E"],`
    - Node `F` connects to `C`, `E`.

37. `}`
    - Ends graph definition.

38. (blank line)

39. `result = bfs_shortest_path(graph, "A", "F")`
    - Calls function to find path from `A` to `F`.

40. `print("BFS shortest path:", " -> ".join(result) if result else "No path")`
    - Prints path like `A -> C -> F`.
    - If result is `None`, prints `No path`.

---

## 2) `dfs.py` - Depth-First Search Path

### What this code does
It finds a path from start to goal using DFS (go deep before backtracking).

### Line-by-line explanation
1. `def dfs_path(graph, start, goal):`
   - Defines DFS function.

2. `    visited = set()`
   - Empty set to remember visited nodes.

3. `    path = []`
   - Current traversal path.

4. (blank line)

5. `    def dfs(node):`
   - Nested helper function for recursion.

6. `        visited.add(node)`
   - Mark current node as visited.

7. `        path.append(node)  # We are currently walking through this node.`
   - Add node to current path.

8. (blank line)

9. `        if node == goal:`
   - If destination reached...

10. `            return True  # Goal found; keep the current path.`
    - Return success.

11. (blank line)

12. `        for nxt in graph[node]:`
    - Explore each neighbor.

13. `            if nxt not in visited and dfs(nxt):`
    - If neighbor is unvisited and recursive DFS from it succeeds...

14. `                return True  # Bubble success up the recursion stack.`
    - Pass success upward.

15. (blank line)

16. `        path.pop()  # Dead end, so remove this node from current path.`
    - Backtracking step.

17. `        return False`
    - This branch did not reach goal.

18. (blank line)

19. `    return path if dfs(start) else None`
    - Start DFS from `start`.
    - Return found path or `None`.

20. (blank line)

21. (blank line)

22. `graph = {`
    - Sample graph.

23. `    "A": ["B", "C"],`
24. `    "B": ["D", "E"],`
25. `    "C": ["F"],`
26. `    "D": [],`
27. `    "E": ["F"],`
28. `    "F": [],`
   - These lines define adjacency lists for each node.

29. `}`
   - End dictionary.

30. (blank line)

31. `result = dfs_path(graph, "A", "F")`
   - Find path from `A` to `F`.

32. `print("DFS path:", " -> ".join(result) if result else "No path")`
   - Print path or `No path`.

---

## 3) `dijkstra.py` - Shortest Path with Edge Weights

### What this code does
Finds the minimum total distance path in a weighted graph (all weights should be non-negative).

### Line-by-line explanation
1. `import heapq`
   - Imports priority queue utilities.

2. (blank line)

3. `def dijkstra(graph, start, end):`
   - Defines Dijkstra function.

4. `    distances = {vertex: float("inf") for vertex in graph}`
   - Sets initial distance of every node to infinity.

5. `    distances[start] = 0`
   - Distance to start node is 0.

6. `    previous = {vertex: None for vertex in graph}`
   - Stores previous node on best known path.

7. `    pq = [(0, start)]  # (distance, node)`
   - Priority queue starts with start node at distance 0.

8. (blank line)

9. `    while pq:`
   - Loop while priority queue is non-empty.

10. `        cur_dist, node = heapq.heappop(pq)`
    - Extract node with smallest distance value.

11. `        if cur_dist > distances[node]:`
    - If queue entry is outdated...

12. `            continue  # Outdated heap entry.`
    - Ignore it.

13. `        if node == end:`
    - If destination popped from queue...

14. `            break`
    - Can stop early.

15. (blank line)

16. `        for nxt, weight in graph[node].items():`
    - Iterate all neighbors and edge weights of current node.

17. `            new_dist = cur_dist + weight`
    - Compute candidate distance via current node.

18. `            if new_dist < distances[nxt]:`
    - If this route is better...

19. `                distances[nxt] = new_dist`
    - Update best known distance.

20. `                previous[nxt] = node`
    - Save predecessor for path reconstruction.

21. `                heapq.heappush(pq, (new_dist, nxt))`
    - Push updated neighbor into priority queue.

22. (blank line)

23. `    if distances[end] == float("inf"):`
    - If end is still unreachable...

24. `        return float("inf"), None`
    - Return infinite distance and no path.

25. (blank line)

26. `    # Follow previous[] from end to start, then reverse.`
    - Comment describing reconstruction.

27. `    path = []`
    - Empty list for path.

28. `    cur = end`
    - Start backtracking from end.

29. `    while cur is not None:`
    - Continue until no predecessor.

30. `        path.append(cur)`
    - Add current node.

31. `        cur = previous[cur]`
    - Move to previous node.

32. `    path.reverse()`
    - Reverse to get start -> end.

33. `    return distances[end], path`
    - Return total distance and path.

34. (blank line)

35. `graph = {`
    - Defines weighted graph as nested dictionary.

36. `    "A": {"B": 4, "C": 2},`
37. `    "B": {"A": 4, "C": 1, "D": 5},`
38. `    "C": {"A": 2, "B": 1, "D": 8, "E": 10},`
39. `    "D": {"B": 5, "C": 8, "E": 2},`
40. `    "E": {"C": 10, "D": 2},`
   - Each key is a node. Each value is `{neighbor: weight}`.

41. `}`
   - End graph definition.

42. (blank line)

43. `dist, path = dijkstra(graph, "A", "E")`
   - Runs algorithm from `A` to `E`.

44. (blank line)

45. `print("Shortest distance:", dist)`
   - Prints shortest numeric distance.

46. `print("Shortest path:", " -> ".join(path) if path else "No path")`
   - Prints route or `No path`.

---

## 4) `krushkal.py` - Kruskal Minimum Spanning Tree

### What this code does
Builds a Minimum Spanning Tree (MST): a subset of edges connecting all vertices with minimum total weight and no cycles.

### Line-by-line explanation
1. `def find(parent, i):`
   - Finds representative (root) of set containing `i`.

2. `    if parent[i] != i:`
   - If `i` is not its own parent, it is not root.

3. `        parent[i] = find(parent, parent[i])  # Path compression.`
   - Recursively find root and compress path for speed.

4. `    return parent[i]`
   - Return root of `i`.

5. (blank line)

6. (blank line)

7. `def union(parent, x, y):`
   - Merges sets of `x` and `y`.

8. `    rx = find(parent, x)`
   - Root of `x`.

9. `    ry = find(parent, y)`
   - Root of `y`.

10. `    if rx != ry:`
    - If they are in different sets...

11. `        parent[ry] = rx  # Join the two components.`
    - Connect one root to the other.

12. (blank line)

13. (blank line)

14. `def kruskal(vertices, edges):`
    - Main Kruskal function.

15. `    parent = list(range(vertices))`
    - Initially each vertex is its own parent/set.

16. `    mst = []`
    - Empty list to collect chosen MST edges.

17. (blank line)

18. `    # Take edges from smallest weight first.`
    - Comment explaining sorting strategy.

19. `    for u, v, w in sorted(edges, key=lambda e: e[2]):`
    - Sort all edges by weight (`e[2]`) ascending.

20. `        if find(parent, u) != find(parent, v):`
    - If edge does not create cycle...

21. `            union(parent, u, v)`
    - Merge components.

22. `            mst.append((u, v, w))`
    - Add edge to MST.

23. `            if len(mst) == vertices - 1:`
    - MST complete when edges count is `V - 1`.

24. `                break`
    - Stop early.

25. `    return mst`
    - Return chosen MST edges.

26. (blank line)

27. (blank line)

28. `vertices = 9`
    - Number of vertices (0 to 8).

29. `edges = [`
    - Start edge list.

30. `	(0, 1, 4), (0, 7, 8),`
31. `	(1, 2, 8), (1, 7, 11),`
32. `	(2, 3, 7), (2, 8, 2), (2, 5, 4),`
33. `	(3, 4, 9), (3, 5, 14),`
34. `	(4, 5, 10),`
35. `	(5, 6, 2),`
36. `	(6, 7, 1), (6, 8, 6),`
37. `	(7, 8, 7),`
   - Each tuple is `(u, v, weight)`.

38. `]`
   - End list.

39. (blank line)

40. `mst = kruskal(vertices, edges)`
   - Compute MST.

41. `print("Edges in the Minimum Spanning Tree:")`
   - Header output.

42. `for u, v, w in mst:`
   - Loop through MST edges.

43. `    print(f"{u} - {v} (weight {w})")`
   - Print each edge using f-string.

---

## 5) `prims.py` - Prim Minimum Spanning Tree

### What this code does
Finds MST by starting from one vertex and repeatedly picking the smallest edge connecting tree to a new vertex.

### Line-by-line explanation
1. `def prim(graph):`
   - Defines Prim algorithm function.

2. `	n = len(graph)`
   - Number of vertices from matrix size.

3. `	in_mst = [False] * n`
   - Boolean list: whether each vertex is in MST.

4. `	in_mst[0] = True  # Start from vertex 0.`
   - Start tree from vertex 0.

5. (blank line)

6. `	mst_edges = []`
   - Stores selected MST edges.

7. `	total = 0`
   - Stores total MST weight.

8. (blank line)

9. `	for _ in range(n - 1):`
   - Need exactly `n-1` edges for MST.

10. `		best_u, best_v = -1, -1`
    - Placeholder for best edge endpoints.

11. `		best_w = float("inf")`
    - Best weight initialized to infinity.

12. (blank line)

13. `		# Pick the lightest edge from chosen set -> unchosen set.`
    - Comment for core logic.

14. `		for u in range(n):`
    - Iterate potential source vertices.

15. `			if in_mst[u]:`
    - Only consider vertices already in MST.

16. `				for v in range(n):`
    - Check all possible destination vertices.

17. `					w = graph[u][v]`
    - Read edge weight from adjacency matrix.

18. `					if w != 0 and not in_mst[v] and w < best_w:`
    - Valid edge must exist (`w != 0`), go to outside vertex, and be lighter.

19. `						best_u, best_v, best_w = u, v, w`
    - Update best edge found so far.

20. (blank line)

21. `		in_mst[best_v] = True`
    - Add chosen new vertex to MST.

22. `		mst_edges.append((best_u, best_v, best_w))`
    - Record chosen edge.

23. `		total += best_w`
    - Add edge weight to total.

24. (blank line)

25. `	return mst_edges, total`
    - Return MST edges and total weight.

26. (blank line)

27. (blank line)

28. `graph = [`
    - Start adjacency matrix.

29. `	[0, 4, 0, 0, 0, 0, 0, 8, 0],`
30. `	[4, 0, 8, 0, 0, 0, 0, 11, 0],`
31. `	[0, 8, 0, 7, 0, 4, 0, 0, 2],`
32. `	[0, 0, 7, 0, 9, 14, 0, 0, 0],`
33. `	[0, 0, 0, 9, 0, 10, 0, 0, 0],`
34. `	[0, 0, 4, 14, 10, 0, 2, 0, 0],`
35. `	[0, 0, 0, 0, 0, 2, 0, 1, 6],`
36. `	[8, 11, 0, 0, 0, 0, 1, 0, 7],`
37. `	[0, 0, 2, 0, 0, 0, 6, 7, 0],`
   - Matrix entry at row `u`, column `v` is edge weight.
   - `0` means no direct edge.

38. `]`
   - End matrix.

39. (blank line)

40. (blank line)

41. `edges, total_weight = prim(graph)`
   - Compute MST from matrix graph.

42. `print("Edges in Prim MST:")`
   - Header line.

43. `for u, v, w in edges:`
   - Loop through selected edges.

44. `    print(f"{u} - {v} (weight {w})")`
   - Print each edge.

45. `print("Total weight:", total_weight)`
   - Print total MST weight.

---

## 6) `sa.py` - Simulated Annealing (Graph Partition)

### Important note about this file
The current file has indentation formatting issues, so Python will raise an `IndentationError` if run exactly as it is now.

The line-by-line explanation below explains the **intended logic** of each line.

### What this code tries to do
It uses Simulated Annealing to find a partition of graph nodes (group 0 or group 1) that minimizes cut size.

### Line-by-line explanation
1. `import random`
   - Imports random number utilities.

2. `import math`
   - Imports math functions (`exp`, etc.).

3. `# Function to calculate cut size`
   - Comment for next function.

4. `def calculate_cut_size(graph, partition):`
   - Function to count edges crossing partitions.

5. `cut_size = 0`
   - Initialize counter.

6. `for u in graph:`
   - Loop through every node `u`.

7. `for v in graph[u]:`
   - Loop through neighbors `v` of `u`.

8. `if partition[u] != partition[v]:`
   - If endpoints are in different groups...

9. `cut_size += 1`
   - Count one crossing edge.

10. `return cut_size // 2 # each edge counted twice`
    - Divide by 2 because undirected edges are seen from both sides.

11. `# Function to generate neighbor solution`
    - Comment.

12. `def generate_neighbor(partition):`
    - Creates nearby solution from current partition.

13. `new_partition = partition.copy()`
    - Copy current partition dictionary.

14. `node = random.choice(list(partition.keys()))`
    - Randomly choose one node.

15. `# Flip the partition of a random node`
    - Comment.

16. `new_partition[node] = 1 - new_partition[node]`
    - If value is 0 becomes 1, if 1 becomes 0.

17. `return new_partition`
    - Return modified partition.

18. `# Simulated Annealing function`
    - Comment.

19. `def simulated_annealing(graph, T=1000, cooling_rate=0.95, T_min=1):`
    - Main optimization function.
    - Parameters:
      - `T`: initial temperature
      - `cooling_rate`: multiply temperature each iteration
      - `T_min`: stop temperature

20. `# Initial random partition (0 or 1)`
    - Comment.

21. `partition = {node: random.randint(0, 1) for node in graph}`
    - Randomly assign every node to partition 0 or 1.

22. `current_cost = calculate_cut_size(graph, partition)`
    - Compute cost of current solution.

23. `best_partition = partition.copy()`
    - Save best solution seen so far.

24. `best_cost = current_cost`
    - Save best cost.

25. `while T > T_min:`
    - Main annealing loop while temperature is high enough.

26. `# Generate new solution`
    - Comment.

27. `new_partition = generate_neighbor(partition)`
    - Make random nearby candidate.

28. `new_cost = calculate_cut_size(graph, new_partition)`
    - Evaluate candidate cost.

29. `# Calculate cost difference`
    - Comment.

30. `delta = new_cost - current_cost`
    - Difference in cost.

31. `# Acceptance condition`
    - Comment.

32. `if delta < 0 or random.random() < math.exp(-delta / T):`
    - Accept if better (`delta < 0`) or sometimes accept worse based on probability.

33. `partition = new_partition`
    - Move to new solution.

34. `current_cost = new_cost`
    - Update current cost.

35. `# Update best solution`
    - Comment.

36. `if current_cost < best_cost:`
    - If improved best known cost...

37. `best_cost = current_cost`
    - Save new best cost.

38. `best_partition = partition.copy()`
    - Save new best partition.

39. `# Cooling schedule`
    - Comment.

40. `T = T * cooling_rate`
    - Lower temperature each iteration.

41. `return best_partition, best_cost`
    - Return best solution found.

42. `# Example graph (Adjacency List)`
    - Comment.

43. `graph = {`
    - Start graph definition.

44. `1: [2, 3, 4],`
45. `2: [1, 3, 5],`
46. `3: [1, 2, 6],`
47. `4: [1, 5],`
48. `5: [2, 4, 6],`
49. `6: [3, 5]`
   - Node-to-neighbors adjacency list.

50. `}`
   - End graph.

51. `# Run Simulated Annealing`
   - Comment.

52. `best_partition, min_cut = simulated_annealing(graph)`
   - Run optimizer and get best partition and minimum cut.

53. `print("Optimal Partition:")`
   - Print heading.

54. `for node in best_partition:`
   - Loop all nodes.

55. `print(f"Node {node} -> Partition {best_partition[node]}")`
   - Print each node's partition assignment.

56. `print("Minimum Cut Size:", min_cut)`
   - Print best cut value.

---

## Python Basics Used in These Files (for absolute beginners)

- `def name(...):`
  - Defines a function.

- `if ...:` / `for ...:` / `while ...:`
  - Control flow statements. The block under them must be indented.

- `list`, `set`, `dict`
  - Basic container types:
    - list: ordered collection, e.g. `[1, 2, 3]`
    - set: unique values, e.g. `{1, 2}`
    - dict: key-value mapping, e.g. `{"A": 1}`

- `return`
  - Sends result back from a function.

- `None`
  - Special value meaning "no value".

- `float("inf")`
  - Represents infinity (a very large value placeholder).

- `f"...{var}..."`
  - f-string: easy way to insert values in text.

---

If you want, I can also create a second README version with:
1. dry-run trace tables (showing variable values at each loop step), and
2. corrected + fully runnable version of `sa.py` with proper indentation.
