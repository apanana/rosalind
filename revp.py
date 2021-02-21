"""
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having
length between 4 and 12. You may return these pairs in any order.
"""

# conversions for bp
conv = {"A":"T",
		"T":"A",
		"C":"G",
		"G":"C"}

def revp(seq):
	for i in range(1,len(seq)-1):
		offset = 0 # number of bases from i that we've checked
		while conv[seq[i-offset]] == seq[i+offset+1]:
			# print(str(i-offset) + " " + str(offset) + ": " + seq[i-offset:i+offset+2])
			offset += 1
			if (i-offset) < 0 or (i+offset+1) == len(seq) or offset*2 >12:
				break
		while offset > 1:
			print(str(i-offset+2) + " " + str(offset*2))
			offset -= 1

# revp("TCAATGCATGCGGGTCTATATGCAT")

f = open("rosalind_revp.txt")
f.readline()
s = ""
for line in f.readlines():
	s += line.strip('\n')
revp(s)