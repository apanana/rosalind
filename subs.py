"""
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""
def subs(s,t):
	locs = []
	for i in range(len(s)-len(t)+1):
		if s[i:i+len(t)] == t:
			locs.append(i+1)
	return locs


"""
Sample Dataset:
GATATATGCATATACTT
ATAT

Sample Output:
2 4 10
"""

# print(subs("GATATATGCATATACTT","ATAT"))

f = open("rosalind_subs.txt","r")
s = f.readline()[:-1]
t = f.readline()[:-1]
print(s)
print(t)
ls = subs(s,t)
for l in ls:
	print l,