
def calculate_cut_size(graph, A, B):
    cut_size = 0
    for i in A:
        for j in B:
            cut_size += graph[i][j]
    return cut_size

def kl_partition(graph):
    n = len(graph)
    A = list(range(n // 2))
    B = list(range(n // 2, n))
    
    print("Initial Partition:")
    print("A:", A)
    print("B:", B)
    initial_cut = calculate_cut_size(graph, A, B)
    print("Initial Cut Size:", initial_cut)
    for i in range(len(A)):
        for j in range(len(B)):
            # Swap nodes
            A[i], B[j] = B[j], A[i]
            
            new_cut = calculate_cut_size(graph, A, B)
            if new_cut > initial_cut:
                A[i], B[j] = B[j], A[i]
            else:
                initial_cut = new_cut
    
    return A, B, initial_cut
graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]
A, B, cut = kl_partition(graph)

print("\nFinal Partition:")
print("Partition A:", A)
print("Partition B:", B)
print("Final Cut Size:", cut)

