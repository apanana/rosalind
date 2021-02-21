"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

def hamm(s,t):
	dH = 0
	for i in range(len(s)):
		if s[i] != t[i]:
			dH += 1
	return dH

f = open("rosalind_hamm.txt","r")
s = f.readline()
t = f.readline()
print(hamm(s,t))