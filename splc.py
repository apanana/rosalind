"""
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings
of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons
of s. (Note: Only one solution will exist for the dataset provided.)
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

def splc(s,ins):
	for intron in ins:
		s = s.replace(intron,"")
	s = s.replace("T","U")
	return prot(s)[:-1]

f = open("rosalind_splc.txt","r")
ins = []
s = ""
for line in f.readlines():
	if line[0] == ">":
		if s != "":
			ins.append(s)
		s = ""
	else:
		s += line.strip('\n')
ins.append(s) #include final intro (not triggered by an extra ">")

print(splc(ins[0],ins[1:]))