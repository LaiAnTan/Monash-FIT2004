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

if __name__ == "__main__":

	v1 = Vertex(1)
	v2 = Vertex(2)
	v3 = Vertex(3)
	v4 = Vertex(4)

	v1.edges = [v2, v3]
	v2.edges = [v1, v4]
	v3.edges = [v1, v4]
	v4.edges = [v2, v3]

	g = Graph()
	g.vertices = [v1, v2, v3, v4]

	print(isTwoColourable(g))  # Expected output: True

