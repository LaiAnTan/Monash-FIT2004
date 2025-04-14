from graph import Graph, Vertex

def isTwoColourable(g: Graph):

	source: Vertex = g.vertices[0]
	source.colour = 0
	source.visited = True

	for v in g.vertices:

		w = 0
		b = 0

		for edge in v.edges:
			if edge.visited == True:
				if edge.colour == 0:
					b += 1
				elif edge.colour == 1:
					w += 1
			else:
				edge.visited = True
				edge.colour = 0 if v.colour == 1 else 1
			
		if b != 0 and w != 0:
			return False
	
	return True

def dfs(source: Vertex):

	if source.visited == True:
		return

	source.visited = True

	for edge in source.edges:
		if edge.visited == False:
			dfs(edge)

def numConnectedComponents(g: Graph):

	components = 0

	for v in g.vertices:
		if v.visited == False:
			dfs(v)
			components += 1
	
	return components

def numValidTwoColourings(g: Graph):

	"""
	if graph is bipartite, num = 2^k where k is number of connected components.
	else num = 0
	"""

	if isTwoColourable(g):
		return 2 ** numConnectedComponents(g)

	return 0

