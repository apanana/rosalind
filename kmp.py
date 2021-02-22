"""
Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.
"""

def kmp(s):
	xs = [0 for x in range(len(s))]
	for i in range(1,len(s)):
		j = 0
		while s[j] == s[i+j]:
			# print(i,j)
			# print(s[:j+1],s[:i+j+1])
			# print(j+1, xs[i+j])
			xs[i+j] = max(j+1, xs[i+j])
			# print(xs)
			# print()
			j += 1
	print(*xs, sep=" ")

# kmp("CAGCATGGTATCACAGCAGAG")
f = open("rosalind_kmp.txt","r")
f.readline() # get rid of first ">"
s = ""
for l in f.readlines():
	s += l.strip("\n")
kmp(s)