# Kruskal's algorithm to find Minimum Spanning Tree (MST)

# Find operation: finds the root of the set in which element i is present
def find(parent, i):
    # Base case: if i is its own parent, it is the root
    if parent[i] == i:
        return i
    # Recursively find the root of the parent
    return find(parent, parent[i])

# Union operation: joins two sets x and y
def union(parent, x, y):
    # Find roots of both sets
    xroot = find(parent, x)
    yroot = find(parent, y)
    # Make one root the parent of the other
    parent[yroot] = xroot

# Kruskal's Algorithm implementation
def kruskal(vertices, edges):
    # Sort all the edges in non-decreasing order of their weight
    edges.sort(key=lambda x: x[2])
    # Create a parent array for union-find, initially each vertex is its own root
    parent = [i for i in range(vertices)]
    mst = []  # Store the resultant MST edges
    
    # Iterate through sorted edges
    for u, v, w in edges:
        # If including this edge doesn't cause a cycle (different roots)
        if find(parent, u) != find(parent, v):
            # Include edge in MST and perform union
            union(parent, u, v)
            mst.append((u, v, w))
    return mst

# Main Program
vertices = 9
# List of edges: (u, v, weight)
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

# Find the MST using Kruskal's algorithm
mst = kruskal(vertices, edges)

# Display the resulting MST edges
print("Edges in the Minimum Spanning Tree:")
for edge in mst:
    print(edge)
