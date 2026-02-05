import sys

# Prim's algorithm to find Minimum Spanning Tree (MST)
def prim(graph, vertices):
    # Array to track selected vertices (initially all False)
    selected = [False] * vertices
    # Start from the first vertex
    selected[0] = True
    
    # Display table header
    print("Edge \tWeight")
    
    # Repeat until we include (vertices-1) edges in the MST
    for _ in range(vertices - 1):
        minimum = sys.maxsize
        x = 0  # Starting vertex of minimum edge
        y = 0  # Ending vertex of minimum edge
        
        # Search for the minimum weight edge connecting a selected node to an unselected node
        for i in range(vertices):
            # If the vertex i is already selected
            if selected[i]:
                for j in range(vertices):
                    # If vertex j is not selected and there is an edge between i and j
                    if not selected[j] and graph[i][j] != 0:
                        # Update minimum weight and coordinates if this edge is smaller
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j
        
        # Print the selected edge and its weight
        print(f"{x} - {y} \t{graph[x][y]}")
        # Mark the end vertex of the selected edge as selected
        selected[y] = True

# Graph represented as an adjacency matrix
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

# Run Prim's algorithm on the graph with 9 vertices
prim(graph, 9)
