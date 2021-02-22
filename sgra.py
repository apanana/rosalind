"""
Given: A list L (of length at most 100) containing positive real numbers.

Return: The longest protein string that matches the spectrum graph of L (if 
multiple solutions exist, you may output any one of them). Consult the 
monoisotopic mass table.
"""

"""
Steps:
1. create graph
2. topo sort graph
3. longest path
"""

# weights = {
# 	71.03711: "A",
# 	103.00919: "C",
# 	115.02694: "D",
# 	129.04259: "E",
# 	147.06841: "F",
# 	57.02146: "G",
# 	137.05891: "H",
# 	113.08406: "I",
# 	128.09496: "K",
# 	113.08406: "L",
# 	131.04049: "M",
# 	114.04293: "N",
# 	97.05276: "P",
# 	128.05858: "Q",
# 	156.10111: "R",
# 	87.03203: "S",
# 	101.04768: "T",
# 	99.06841: "V",
# 	186.07931: "W",
# 	163.06333: "Y", 
# }

weights = {
	71.0371: "A",
	103.0092: "C",
	115.0269: "D",
	129.0426: "E",
	147.0684: "F",
	57.0215: "G",
	137.0589: "H",
	113.0841: "I",
	128.0950: "K",
	113.0840: "L",
	131.0405: "M",
	114.0429: "N",
	97.0528: "P",
	128.0586: "Q",
	156.1011: "R",
	87.0320: "S",
	101.0477: "T",
	99.0684: "V",
	186.0793: "W",
	163.0633: "Y", 
}

def topo_sort_helper(nodes, edges, n, ts_nodes):
	if n not in nodes:
		return
	nodes.remove(n)
	for t in edges.get(n,[]):
		topo_sort_helper(nodes, edges, t, ts_nodes)
	ts_nodes.append(n)


def topo_sort(nodes, edges):
	ts_nodes = []
	while nodes != []:
		topo_sort_helper(nodes, edges, nodes[0], ts_nodes)
	return ts_nodes[::-1]

def longest_path(ts_nodes, edges):
	# calculate distances
	dist = {n: -1 for n in ts_nodes}
	preceding = {n: 0.0 for n in ts_nodes}
	for n in ts_nodes:
		for t in edges.get(n,[]):
			if dist[t] < dist[n] + 1:
				dist[t] = dist[n] + 1
				preceding[t] = n

	# find furthest node
	max_d = -1
	max_node = 0
	for n, d in dist.iteritems():
		if d > max_d:
			max_d = d
			max_node = node

	# recreate path
	path = []
	while max_d != -1:
		path.append((preceding[max_node], max_node))
		max_node = preceding[max_node]
		max_d = dist[max_node]

	return path[::-1]

def prot(path):
	# create string
	ps = ""
	for (s,t) in path:
		ps += weights[round(t-s,4)]
	return ps

f = open("rosalind_sgra.txt","r")
nodes = []
edges = {}
for line in f.readlines():
	n = float(format(line.strip('\n')))
	nodes.append(n)
	for node in nodes:
		if weights.get(round(n-node,4),"") != "":
			edges.setdefault(node,[]).append(n)

# topological sort
ts_nodes = topo_sort(nodes,edges)

# find longest path
path = longest_path(ts_nodes, edges)

# find protein string
print(prot(path))
