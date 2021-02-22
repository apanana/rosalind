"""
Given: A positive integer n (n<=1000) and an adjacency list corresponding to a
graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a
tree.
"""

# overall: do a BFS while counting how many edges we add
# start with lowest node and do BFS. if search is completed and nodes 
# are remaining, add an edge from  lowest node to lowest unfound node 
# and resume search.
# once all nodes are found, report number of edges added
def tree(nodes, edges):
	count = 0
	q = []
	while nodes != []:
		q.append(nodes[0])
		nodes.remove(nodes[0])
		while q != []:
			ws = edges.get(q[0],[])
			# print(q[0], ws, q, nodes)
			for w in ws:
				if w in nodes:
					q.append(w)
					nodes.remove(w)
			q.remove(q[0])
			# print(q, nodes, count)
			# print
		count += 1
	return count-1 # adds an extra 1 after last iter


f = open("rosalind_tree.txt","r")

n = f.readline()
nodes = [x+1 for x in range(int(n))]
edges = {}
for line in f.readlines():
	st = line.strip('\n').split(" ")
	edges.setdefault(int(st[0]),[]).append(int(st[1]))
	edges.setdefault(int(st[1]),[]).append(int(st[0]))

print(tree(nodes,edges))
