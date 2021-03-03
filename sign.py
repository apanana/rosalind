"""
Given: A positive integer n<=6.

Return: The total number of signed permutations of length n, followed by a list
of all such permutations (you may list the signed permutations in any order).
"""

def signed_perm_help(fixed, to_perm):
	# nothing left to permute
	if len(to_perm) == 1:
		return [2, [fixed+[-to_perm[0]], fixed+to_perm]] # bc fuck space efficiency amirite? :D
	# fix one number from to_perm and permute on the remaining numbers
	else:
		records = [0, []]
		for i in to_perm:
			rec = signed_perm_help(fixed+[-i],[x for x in to_perm if x != i])
			records[0] += rec[0]
			records[1] += rec[1]
			rec = signed_perm_help(fixed+[i],[x for x in to_perm if x != i])
			records[0] += rec[0]
			records[1] += rec[1]
		return records

def sign(n):
	ps = signed_perm_help([],[i+1 for i in range(n)])
	print(ps[0])
	for p in ps[1]:
		print(*p, sep=" ")

sign(5)
