"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the 
GC-content of that string. Rosalind allows for a default error of 0.001 in all 
decimal answers unless otherwise stated; please see the note on absolute error 
below.
"""
from __future__ import division

def gc(s):
	if len(s) == 0:
		return 0
	g = s.count("G")
	c = s.count("C")
	return (g+c)/len(s)*100

f = open("rosalind_gc.txt","r")
highest_id = ""
highest_gc = 0
current_dna = ""
current_id = ""
for line in f.readlines():
	if line[0] == ">":
		# compare max and update
		current_gc = gc(current_dna)
		if current_gc > highest_gc:
			highest_gc = current_gc
			highest_id = current_id
		# reset dna_string and current_id
		current_dna = ""
		current_id = line[1:-1]
	else:
		current_dna += line[:-1]

# check last id and dna
current_gc = gc(current_dna)
if current_gc > highest_gc:
	highest_gc = current_gc
	highest_id = current_id

print highest_id
print highest_gc

"""
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

"""
Rosalind_0808
60.919540
"""