"""
Given: At most 50 DNA strings of approximately equal length, not exceeding
1 kbp, in FASTA format (which represent reads deriving from the same strand of a
single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a
unique way to reconstruct the entire chromosome from these reads by gluing
together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus
corresponding to a reconstructed chromosome).
"""


"""
can definitely find the two ends:
left side is substr without any overlap with other right sides
right side is substr without any overlap with other left sides
-----
not sure how to prove if greedy is sufficient :(
-----
table Aij = earlier index in s_i(left) that has overlap with s_j(right) OR -1

finding start = find the i st Asi = -1 for all s
finding end = find i st Ait = -1 for all t

find shortest path from s to t that spans graph

would probably work, is probably overly complicated
----
greedy:
find next substr with greatest overlap with current substr, add it on

intuitively i think it would work bc of the >half overlap but not sure how to
state the logic
"""

def shortest_superstring(strs):
	sup = strs[0]
	strs.remove(strs[0])
	left = False
	right = False
	while len(strs) > 0:
		print(sup, strs)
		# compare left side of superstring with right sides of all strings
		if not left:
			print("LEFT")
			max_overlap = 0
			max_str = ""
			for st in strs:
				# print("sup: " + sup + ", st: " + st)
				width = min(len(sup),len(st))
				for i in range(width//2,width):
					if len(sup[:i]) != len(st[-i:]):
						print("lens no equal")
						print(sup[:i],st[-i:])
						print()
						return
					if sup[:i] == st[i]:
						if i > max_overlap:
							max_overlap = i
							max_str = st
			if max_str != "":
				sup = max_str + sup[max_overlap:]
				strs.remove(max_str)
				print("max overlap:")
				print(max_str,max_overlap)
				print
			else:
				left = True
		# compare right side of superstring with left side of all strings
		if not right:
			print("RIGHT")
			max_overlap = 0
			max_str = ""
			for st in strs:
				width = min(len(sup),len(st))
				# print("sup: " + sup + ", st: " + st)
				# print("width: " + str(width) + " len(sup):" + str(len(sup)) + " len(st):" + str(len(st)))
				for i in range(width//2):
					if len(sup[-width//2-i:]) != len(st[:width//2+i]):
						print("lens no equal")
						print(width, i, width//2-i, width//2+i)
						print(sup[-width//2-i:],st[:width//2+i])
						print()
						return
					# print(i,width//2-i,sup[-width//2-i:],st[:width//2+i])
					if sup[-width//2-i:] == st[:width//2+i]:
						if (-width//2-i) < max_overlap:
							max_overlap = -width//2-i
							max_str = st
			if max_str != "":
				print("CONSTRUCT NEW STRING")
				print(sup, max_str,max_overlap)
				sup = sup[:max_overlap] + max_str
				strs.remove(max_str)
				print("max overlap:")
				print(max_str,max_overlap)
				print
	return sup

f = open("rosalind_long.txt","r")
strs = []
s = ""
for line in f.readlines():
	if line[0] == ">":
		if s != "":
			strs.append(s)
		s = ""
	else:
		s += line.strip('\n')
strs.append(s)

expected = "ATTAGACCTGCCGGAATAC"
calc = shortest_superstring(strs)
print("RESULTS:")
print(expected)
print(calc)
print(expected==calc)
