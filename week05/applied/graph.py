
class Vertex:

	def __init__(self, value):
		self.value = value
		self.edges: list[Vertex] = []
		self.colour = None # 0 black, 1 white
		self.visited = False

class Graph:

	def __init__(self):
		
		self.vertices = []