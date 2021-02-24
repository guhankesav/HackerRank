
from collections import defaultdict




class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [] 

	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

    # def deledge(self,u,v):
    #     self.graph.pop([u,v])
	# A utility function to find set of an element i

	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])


	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)


		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot


		else:
			parent[yroot] = xroot
			rank[xroot] += 1


	def KruskalMST(self):

		result = [] 
		
		i = 0
		
		e = 0


		self.graph = sorted(self.graph, 
							key=lambda item: item[2])

		parent = []
		rank = []

		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		while e < self.V - 1:


			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)


			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)

		minimumCost = 0
		for u, v, weight in result:
			minimumCost += weight
		print(minimumCost)

n = input()
k=input()
g = Graph(n)
for i in range(n):
    ki=input()
    x = ki.split()
    g.addEdge(x[0],x[1],x[2])

ans = 0 
for i in range(k):
    ki=input()
    x = ki.split()
    a = x[0] + (ans % 100)
    b = x[1] + (ans % 100)
    u = x[2] + (ans % 100)
    v = x[3] + (ans % 100)
    c = x[4] + (ans % 100)
    g.deledge(a,b)
    g.addEdge(u,v,c)


g.KruskalMST()

