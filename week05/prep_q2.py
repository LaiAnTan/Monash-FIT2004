

class DirectedEdgeVertex:

	def __init__(self, value):
		
		self.edges: list[DirectedEdgeVertex] = []
		self.visited = False
		self.value = value
	
	def __repr__(self):
		return str(self.value)

	def addDirectedEdges(self, list: list["DirectedEdgeVertex"]):

		self.edges = list

def allReachableVerticesAux(curr: DirectedEdgeVertex,
	reachable: list[DirectedEdgeVertex]):

	curr.visited = True
	reachable.append(curr)

	if len(curr.edges) == 0:
		return

	for edge in curr.edges:
		if edge.visited == False:
			allReachableVerticesAux(edge, reachable)

def allReachableVertices(source: DirectedEdgeVertex):

	reachable = []

	allReachableVerticesAux(source, reachable)

	return reachable

if __name__ == "__main__":

	v = [DirectedEdgeVertex(i) for i in range(9)]

	print(v)

	v[0].addDirectedEdges([v[1], v[7]])
	v[1].addDirectedEdges([v[2]])
	v[2].addDirectedEdges([v[3]])
	v[3].addDirectedEdges([v[4]])
	v[4].addDirectedEdges([v[5]])
	v[5].addDirectedEdges([v[6]])
	v[7].addDirectedEdges([v[8]])
	v[8].addDirectedEdges([v[3]])

	print(allReachableVertices(v[0]))