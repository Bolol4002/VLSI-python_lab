# Find operation
def find(parent, i):
	if parent[i] == i:
		return i
	return find(parent, parent[i])
# Union operation
def union(parent, x, y):
	xroot = find(parent, x)
	yroot = find(parent, y)
	parent[yroot] = xroot
# Kruskal's Algorithm
def kruskal(vertices, edges):
	edges.sort(key=lambda x: x[2])
	parent = [i for i in range(vertices)]
	mst = []
	for u, v, w in edges:
		if find(parent, u) != find(parent, v):
			union(parent, u, v)
			mst.append((u, v, w))
	return mst
# Main Program
vertices = 9
edges = [
	(0, 1, 4), (0, 7, 8),
	(1, 2, 8), (1, 7, 11),
	(2, 3, 7), (2, 8, 2), (2, 5, 4),
	(3, 4, 9), (3, 5, 14),
	(4, 5, 10),
	(5, 6, 2),
	(6, 7, 1), (6, 8, 6),
	(7, 8, 7)
]
mst = kruskal(vertices, edges)
print("Edges in the Minimum Spanning Tree:")
for edge in mst:
	print(edge)
