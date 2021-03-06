"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
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
		l = RNA_CODON_TABLE[s[i:i+3]]
		if l == "Z":
			break
		else:
			p += l
		i += 3
	return p

# print(prot("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))

f = open("rosalind_prot.txt","r")
print(prot(f.readline()))