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

def len_overlap(s1,s2):
	# compares left of s1 to right of s2
	w = min(len(s1),len(s2))
	while w > min(len(s1)//2,len(s2)//2):
		if s1[:w] == s2[-w:]:
			return w
		else:
			w -= 1
	return 0

def shortest_superstring(strs):
	sup = strs[0]
	strs.remove(strs[0])
	# once we find the right edge, search towards the left
	right = False
	while len(strs) > 0:
		max_overlap = 0
		max_str = ""
		for st in strs:
			w = len_overlap(st,sup) if (not right) \
									else len_overlap(sup,st)
			if w > max_overlap:
				max_overlap = w
				max_str = st
		if max_str != "":
			sup = (sup[:-max_overlap] + max_str) if (not right) \
									else (max_str + sup[max_overlap:])
			strs.remove(max_str)
		else:
			right = True
	return sup

# def shortest_superstring(strs):
# 	sup = strs[0]
# 	strs.remove(strs[0])
# 	# save ourselves a bit of time once we find an edge
# 	left = False
# 	right = False
# 	while len(strs) > 0:
# 		# compare left side of superstring with right sides of all strings
# 		if not left:
# 			max_overlap = 0
# 			max_str = ""
# 			for st in strs:
# 				w = min(len(sup),len(st))
# 				while w > min(len(st)//2,len(sup)//2):
# 					if st[-w:] == sup[:w]:
# 						if w > max_overlap:
# 							max_overlap = w
# 							max_str = st
# 					w -=1
# 			if max_str != "":
# 				sup = max_str + sup[max_overlap:]
# 				strs.remove(max_str)
# 			else:
# 				left = True
# 		# compare right side of superstring with left side of all strings
# 		if not right:
# 			max_overlap = 0
# 			max_str = ""
# 			for st in strs:
# 				w = min(len(sup),len(st))
# 				while w > min(len(st)//2,len(sup)//2):
# 					if sup[-w:] == st[:w]:
# 						if w > max_overlap:
# 							max_overlap = w
# 							max_str = st
# 					w -= 1
# 			if max_str != "":
# 				sup = sup[:-max_overlap] + max_str
# 				strs.remove(max_str)
# 			else:
# 				right = True
# 	return sup

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
res = shortest_superstring(strs)
print(res)
