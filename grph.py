"""
Given: A collection of DNA strings in FASTA format having total length at most
10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any
order.
"""

f = open("rosalind_grph.txt","r")

pfx_dict = {}
sfx_dict = {}
name = ""
bps = ""

# bps may go over multiple lines (10kbp)
for line in f.readlines():
	if line[0] == ">":
		if bps != "":
			pfx_dict.setdefault(bps[:3],[]).append(name)
			sfx_dict.setdefault(bps[-3:],[]).append(name)
			bps = ""
		name = line.strip('\n')[1:]
	else:
		bps += line.strip('\n')
# one more time after end of file
pfx_dict.setdefault(bps[:3],[]).append(name)
sfx_dict.setdefault(bps[-3:],[]).append(name)	

edges = []
for sfx in sfx_dict.keys():
	if len(pfx_dict.get(sfx,[])) != 0:
		for s in sfx_dict[sfx]:
			for t in pfx_dict[sfx]:
				if s != t: #no self-edges
					edges.append(s + " " + t)

for e in edges:
	print(e)
