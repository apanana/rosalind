"""
Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs
of s. Strings can be returned in any order.
"""

RNA_CODON_TABLE = {
 "UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
 "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
 "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
 "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
 "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
 "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
 "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
 "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
 "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
 "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
 "UAA":"Z", "CAA":"Q", "AAA":"K", "GAA":"E",
 "UAG":"Z", "CAG":"Q", "AAG":"K", "GAG":"E",
 "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
 "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
 "UGA":"Z", "CGA":"R", "AGA":"R", "GGA":"G",
 "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G",
	}

def prot(s):
	i = 0
	p = ""
	while i < len(s):
		if len(s[i:i+3]) < 3:
			break
		p += RNA_CODON_TABLE[s[i:i+3]]
		i += 3
	return p

def revc(s):
	t = ""
	for base in s:
		if base == "A":
			t += "U"
		elif base == "C":
			t += "G"
		elif base =="G":
			t += "C"
		elif base == "U":
			t += "A"
	return t[::-1]

def find_prots(s, prots):
	for i in range(len(s)):
		if s[i] == "M":
			try:
				j = s.index("Z",i)
			except:
				return
			prots.add(s[i:j])

# s = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
 
f = open("rosalind_orf.txt","r")
f.readline() #get rid of first ">"
s = ""
for line in f.readlines():
	s += line.strip('\n')
s = s.replace("T","U")

# find all proteins
prots = set()
find_prots(prot(s), prots)
find_prots(prot(revc(s)), prots)
find_prots(prot(s[1:]), prots)
find_prots(prot(revc(s[:-1])), prots)
find_prots(prot(s[2:]), prots)
find_prots(prot(revc(s[:-2])), prots)

# print
for p in prots:
	print(p)
