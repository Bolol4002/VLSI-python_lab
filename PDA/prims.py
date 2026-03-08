import sys


def prim(graph, vertices):
	selected = [False] * vertices
	selected[0] = True
	print("Edge \tWeight")
	for _ in range(vertices - 1):
		minimum = sys.maxsize
		x = 0
		y = 0
		for i in range(vertices):
			if selected[i]:
				for j in range(vertices):
					if not selected[j] and graph[i][j] != 0:
						if graph[i][j] < minimum:
							minimum = graph[i][j]
							x = i
							y = j
		print(f"{x} - {y} \t{graph[x][y]}")
		selected[y] = True


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


prim(graph, 9)
