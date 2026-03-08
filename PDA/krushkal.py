def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])  # Path compression.
    return parent[i]


def union(parent, x, y):
    rx = find(parent, x)
    ry = find(parent, y)
    if rx != ry:
        parent[ry] = rx  # Join the two components.


def kruskal(vertices, edges):
    parent = list(range(vertices))
    mst = []

    # Take edges from smallest weight first.
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
            if len(mst) == vertices - 1:
                break
    return mst


vertices = 9
edges = [
	(0, 1, 4), (0, 7, 8),
	(1, 2, 8), (1, 7, 11),
	(2, 3, 7), (2, 8, 2), (2, 5, 4),
	(3, 4, 9), (3, 5, 14),
	(4, 5, 10),
	(5, 6, 2),
	(6, 7, 1), (6, 8, 6),
	(7, 8, 7),
]

mst = kruskal(vertices, edges)
print("Edges in the Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v} (weight {w})")
