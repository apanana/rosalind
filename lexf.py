"""
Given: A collection of at most 10 symbols defining an ordered alphabet, and a
positive integer n (n<=10).

Return: All strings of length n that can be formed from the alphabet, ordered
lexicographically (use the standard order of symbols in the English alphabet).
"""

# def lexf_helper(s,syms,n):
# 	if n == 0:
# 		return [s]
# 	else:
# 		strs = []
# 		i = syms.index(s[-1]) if len(s) > 0 else 0
# 		for sym in syms[i:]:
# 			strs += lexf_helper(s+sym, syms, n-1)
# 		return strs

# def lexf(syms,n):
# 	return lexf_helper("",syms,n)
"""
whoops that solves a totally different problem T_T
"""
def lexf(syms,n):
	def lexf_helper(s, syms, n):
		if n == 0:
			return [s]
		else:
			strs = []
			for sym in syms:
				strs += lexf_helper(s+sym, syms, n-1)
			return strs

	return lexf_helper("",syms,n)

f = open("rosalind_lexf.txt","r")
syms = [sym for sym in f.readline().strip('\n').split(" ")]
n = int(f.readline().strip('\n'))

strs = lexf(syms,n)
for s in strs:
	print(s)
