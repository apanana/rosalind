"""
Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.
"""
### soln from LEXF 
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

def kmer(k,s):
	strs = lexf(["A","C","G","T"],k)
	counts = [0]*len(strs)
	for i in range(len(s)-k+1):
		counts[strs.index(s[i:i+k])] += 1
	return counts



f = open("rosalind_kmer.txt","r")
f.readline() # skip ">"
s = ""
for line in f.readlines():
	s += line.strip('\n')

print(*kmer(4,s))

# ks = kmer(4,s)
# ans = "4 1 4 3 0 1 1 5 1 3 1 2 2 1 2 0 1 1 3 1 2 1 3 1 1 1 1 2 2 5 1 3 0 2 2 1 1 1 1 3 1 0 0 1 5 5 1 5 0 2 0 2 1 2 1 1 1 2 0 1 0 0 1 1 3 2 1 0 3 2 3 0 0 2 0 8 0 0 1 0 2 1 3 0 0 0 1 4 3 2 1 1 3 1 2 1 3 1 2 1 2 1 1 1 2 3 2 1 1 0 1 1 3 2 1 2 6 2 1 1 1 2 3 3 3 2 3 0 3 2 1 1 0 0 1 4 3 0 1 5 0 2 0 1 2 1 3 0 1 2 2 1 1 0 3 0 0 4 5 0 3 0 2 1 1 3 0 3 2 2 1 1 0 2 1 0 2 2 1 2 0 2 2 5 2 2 1 1 2 1 2 2 2 2 1 1 3 4 0 2 1 1 0 1 2 2 1 1 1 5 2 0 3 2 1 1 2 2 3 0 3 0 1 3 1 2 3 0 2 1 2 2 1 2 3 0 1 2 3 1 1 3 1 0 1 1 3 0 2 1 2 2 0 2 1 1"
# ans = [int(a) for a in ans.split(" ")]
# lex = lexf(["A","C","G","T"],4)

# print(len(ks), len(ans), len(lex))
# for i in range(len(ks)):
# 	if ks[i] != ans[i]:
# 		print(i, ks[i],ans[i], lex[i])
