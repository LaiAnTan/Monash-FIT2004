from graph import Graph, Vertex

def hasCycleAux(curr: Vertex, start: Vertex):

	if curr == start:
		return True

	curr.visited = True

	for edge in curr.edges:
		if edge.visited == False:
			return hasCycleAux(edge, start)
	
	return False

def hasCycle(g: Graph): # g is directed

	for v in g.vertices:
		if v.visited == False:
			if hasCycleAux(v, v):
				return True

	return False

if __name__ == "__main__":

	v1 = Vertex(1)
	v2 = Vertex(2)
	v3 = Vertex(3)
	v4 = Vertex(4)

	v1.edges = [v2]
	v2.edges = [v3]
	v3.edges = [v4]
	v4.edges = []

	g = Graph()
	g.vertices = [v1, v2, v3, v4]

	print(hasCycle(g))