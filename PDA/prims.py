def prim(graph):
	visited = []
	for i in range(graph[0]):
		visited[i]=False

	visited[0]=true
	mst=0
	for i in graph:
		for j in i:
			w = graph[i][j]
			if(w>graph[i][0]+graph[j][0]):
				mst=graph[i][0]+graph[j][0]
			else:
				mst+=w
			visted[i]=true
	return mst

graph = [
	[0, 2, 7, 0],
	[2, 0, 1, 8],
	[7, 1, 0, 3],
	[0, 8, 3, 0],
]


edges, total_weight = prim(graph)
print("MST of the grapth is :")
print("MST:", total_weight)+9*9*9