"""
Given: A collection of k (k<=100) DNA strings of length at most 1 kbp each in
FASTA format.

Return: A longest common substring of the collection. (If multiple solutions
exist, you may return any single solution.)
"""

"""
For strings k1,...,kn, let the set of all common substrings between ki and kj
be Cij. Fix an i (e.g. i=1), and find the all n-1 subsets Cij(j!=i). If we take
the intersection of all these subsets, the longest substring in the set will be
the longest common substring.

Q: runtime of finding all common substrings. For a strings of length l and k,
we could get all substrings of each string in O(l^2) and O(k^2) time and then
take the intersection which is O(min(l^2,k^2)) [size of the sets]. So, overall
runtime is going to be O(max(l^2,k^2)). We know this is bounded to 1000 :)
"""

def substrings(k):
	S = set()
	for i in range(len(k)):
		for j in range(i+1,len(k)+1):
			S.add(k[i:j])
	return S

def lcsm(ks):
	k1 = substrings(ks[0])
	for k in ks:
		kj = substrings(k)
		k1 = k1 & kj
	max_len = 0
	max_str = ""
	for substring in k1:
		if len(substring) > max_len:
			max_str = substring
			max_len = len(substring)
	return max_str


f = open("rosalind_lcsm.txt","r")
ks = []
s = ""
for line in f.readlines():
	if line[0] == ">":
		if s != "":
			ks.append(s)
		s = ""
	else:
		s += line.strip('\n')
ks.append(s) #include final intro (not triggered by an extra ">")

print(lcsm(ks))
