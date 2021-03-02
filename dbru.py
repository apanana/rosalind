"""
Given: A collection of up to 1000 (possibly repeating) DNA strings of equal
length (not exceeding 50 bp) corresponding to a set S of (k+1)-mers.

Return: The adjacency list corresponding to the de Bruijn graph corresponding to
SuSrc.
"""

def revc(s):
	t = ""
	for base in s:
		if base == "A":
			t += "T"
		elif base == "C":
			t += "G"
		elif base =="G":
			t += "C"
		elif base == "T":
			t += "A"
	return t[::-1]

def dbru(xs):
	S = set([])
	for x in xs:
		S.add(x)
		S.add(revc(x))
	edges = set([])
	for kp1 in S:
		edges.add((kp1[:-1],kp1[1:]))
	edges = list(edges)
	edges.sort()
	return edges



f = open("rosalind_dbru.txt","r")
xs = []
for line in f.readlines():
	xs.append(line.strip('\n'))

edges = dbru(xs)
for edge in edges:
	print('(%s)' % ', '.join(map(str, edge)))
