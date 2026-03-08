def prim(graph):
	n = len(graph)
	in_mst = [False] * n
	in_mst[0] = True  # Start from vertex 0.

	mst_edges = []
	total = 0

	for _ in range(n - 1):
		best_u, best_v = -1, -1
		best_w = float("inf")

		# Pick the lightest edge from chosen set -> unchosen set.
		for u in range(n):
			if in_mst[u]:
				for v in range(n):
					w = graph[u][v]
					if w != 0 and not in_mst[v] and w < best_w:
						best_u, best_v, best_w = u, v, w

		in_mst[best_v] = True
		mst_edges.append((best_u, best_v, best_w))
		total += best_w

	return mst_edges, total


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


edges, total_weight = prim(graph)
print("Edges in Prim MST:")
for u, v, w in edges:
    print(f"{u} - {v} (weight {w})")
print("Total weight:", total_weight)
