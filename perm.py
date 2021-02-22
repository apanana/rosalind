"""
Given: A positive integer n<=7

Return: The total number of permutations of length n, followed by a list of all
such permutations (in any order).
"""

def perm_help(fixed, to_perm):
	# nothing left to permute
	if len(to_perm) == 1:
		return [1, [fixed+to_perm]] # bc fuck space efficiency amirite? :D
	# fix one number from to_perm and permute on the remaining numbers
	else:
		records = [0, []]
		for i in to_perm:
			rec = perm_help(fixed+[i],[x for x in to_perm if x != i])
			records[0] += rec[0]
			records[1] += rec[1]
		return records


def perm(n):
	ps = perm_help([],[i+1 for i in range(n)])
	print(ps[0])
	for p in ps[1]:
		print(*p, sep=" ")

# perm(7) 
# output is a few thousand lines long
# run with `python3 perm.py > out.txt`