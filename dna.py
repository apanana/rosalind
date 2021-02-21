"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of 
times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""
def dna(s):
	counts = [0,0,0,0]
	for base in s:
		if base == "A":
			counts[0] += 1
		elif base == "C":
			counts[1] += 1
		elif base =="G":
			counts[2] += 1
		elif base == "T":
			counts[3] += 1
		else:
			print("hi")
	for c in counts:
		print c,

# s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
# dna(s)

f = open("rosalind_dna.txt","r")
x = f.readline()
print(x)
dna(x)
