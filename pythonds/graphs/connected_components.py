def dfs(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	visit.add(start)
	for next in graph[start] - visited:
		dfs(graph, next, visited)
	return  visited

# central set to keep track of visited nodes
visit = set()

if __name__ == "__main__":
	graph = {
		0: set([1, ]),
		1: set([0, 2]),
		2: set([1, ]), 
		3: set([4, ]),
		4: set([3, ]),
	}
	nodes = [node for node in graph.keys()]
	for node in nodes:
		if node not in visit:
			print(dfs(graph, node))
	# print(dfs(graph, 0))