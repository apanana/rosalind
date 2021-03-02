"""
Given: A collection of (error-free) DNA k-mers (k<=50) taken from the same
strand of a circular chromosome. In this dataset, all k-mers from this strand of
the chromosome are present, and their de Bruijn graph consists of exactly one
simple cycle.

Return: A cyclic superstring of minimal length containing the reads (thus
corresponding to a candidate cyclic chromosome).
"""

def pcov(ks):
	edges = set([])
	for k in ks:
		edges.add((k[:-1],k[1:]))
	adj = {}
	for edge in edges:
		adj[edge[0]] = edge[1]
	start = adj.keys()[0]
	next = adj[start]
	min_str = start[0]
	while next != start:
		min_str += next[0]
		next = adj[next]
	return min_str

f = open("rosalind_pcov.txt","r")
ks = []
for line in f.readlines():
	ks.append(line.strip('\n'))

print(pcov(ks))
