import random
import math

# Function to calculate cut size
def calculate_cut_size(graph, partition):
    cut_size = 0
    for u in graph:
        for v in graph[u]:
            if partition[u] != partition[v]:
                cut_size += 1
    return cut_size // 2  # each edge counted twice


# Function to generate neighbor solution
def generate_neighbor(partition):
    new_partition = partition.copy()
    node = random.choice(list(partition.keys()))
    
    # Flip the partition of a random node
    new_partition[node] = 1 - new_partition[node]
    return new_partition


# Simulated Annealing function
def simulated_annealing(graph, T=1000, cooling_rate=0.95, T_min=1):
    
    # Initial random partition (0 or 1)
    partition = {node: random.randint(0, 1) for node in graph}

    current_cost = calculate_cut_size(graph, partition)
    best_partition = partition.copy()
    best_cost = current_cost

    while T > T_min:
        # Generate new solution
        new_partition = generate_neighbor(partition)
        new_cost = calculate_cut_size(graph, new_partition)

        # Calculate cost difference
        delta = new_cost - current_cost

        # Acceptance condition
        if delta < 0 or random.random() < math.exp(-delta / T):
            partition = new_partition
            current_cost = new_cost

        # Update best solution
        if current_cost < best_cost:
            best_cost = current_cost
            best_partition = partition.copy()

        # Cooling schedule
        T = T * cooling_rate

    return best_partition, best_cost


# Example graph (Adjacency List)
graph = {
    1: [2, 3, 4],
    2: [1, 3, 5],
    3: [1, 2, 6],
    4: [1, 5],
    5: [2, 4, 6],
    6: [3, 5]
}


# Run Simulated Annealing
best_partition, min_cut = simulated_annealing(graph)

print("Optimal Partition:")
for node in best_partition:
    print(f"Node {node} -> Partition {best_partition[node]}")

print("Minimum Cut Size:", min_cut)