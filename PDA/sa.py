import random
import math

def calculate_cut_size(graph, partition):
    cut_size = 0
    for u in graph:
        for v in graph[u]:
            if partition[u] != partition[v]:
                cut_size += 1
    return cut_size // 2  # each edge counted twice

def generate_neighbor(partition):
    new_partition = partition.copy()
    node = random.choice(list(partition.keys()))
    
    new_partition[node] = 1 - new_partition[node]
    return new_partition

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
    
graph = {
    1: [2, 3, 4],
    2: [1, 3, 5],
    3: [1, 2, 6],
    4: [1, 5],
    5: [2, 4, 6],
    6: [3, 5]
}
best_partition, min_cut = simulated_annealing(graph)

print("Optimal Partition:")
for node in best_partition:
    print(f"Node {node} -> Partition {best_partition[node]}")

print("Minimum Cut Size:", min_cut)