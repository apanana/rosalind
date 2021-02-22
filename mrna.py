"""
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could
have been translated, modulo 1,000,000. (Don't neglect the importance of the
stop codon in protein translation.)
"""

CODON_COUNTS = {
	"A": 4,
	"C": 2,
	"D": 2,
	"E": 2,
	"F": 2,
	"G": 4,
	"H": 2,
	"I": 3,
	"K": 2,
	"L": 6,
	"M": 1,
	"N": 2,
	"P": 4,
	"Q": 2,
	"R": 6,
	"S": 6,
	"T": 4,
	"V": 4,
	"W": 1,
	"Y": 2,
	"Z": 3,
}

def mrna(cs):
	prod = 1
	for c in cs+"Z":
		prod *= CODON_COUNTS[c]
		prod %= 1000000
	return prod

f = open("rosalind_mrna.txt","r")
cs = f.readline().strip('\n')
print(mrna(cs))
