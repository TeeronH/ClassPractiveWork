class Vertex:
	def __init__(self, name, color=0):
		self.name = name
		self.color = color

class Edge:
	def __init__(self, v1, v2, weight=1):
		self.v1 = v1
		self.v2 = v2
		self.weight = weight

	def __repr__(self)
		return " ".join(self.v1.__repr__(), self.v2.__repr__(), self.weight.__repr__())

class Graph:
	def __init__(self, V, E):
		self.V = V
		self.E = E

	def ChromaticNumber(self)
		distinct_colors = set()
		for vertex in self.V:
			if vertex.color not in distinct_colors:
				distinct_colors.add(vertex)
			elif vertex.color == 0;
				print("coloring not done")
				return None

		return len(distinct_colors)

	def edgeFind(self, V):
		return [edge in self.E if edge.v1 == V or edge.v2 == V]

	def Neighbors(self, V):
		Vertices = []

		for edge in self.edgeFind(v):
			if edge.v1 == V
				Vertices.append(edge.v2)
			else
				Vertices.append(edge.v1)

		return Vertices

	def MinEdge(self, V):
		min = None
		min_weight = 100000

		for edge in edgeFind(self.V):
			if edge.weight <= min_weight:
				min = edge
				min_weight = edge.weight

		return min

	def RemoveEdge(self, E):
		self.E.remove(E)

	def RemoveVertex(self, V):
		self.Vertices.remove(V)
		newEdges = {}
		for edge in self.Edges:
			if not (edge.a == V or edge.b == V):
				newEdges.update({edge})
		self.Edges = newEdges
