"""
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""
from requests import get

base_url = "http://www.uniprot.org/uniprot/"
def mprt(motif):
	url = base_url + motif + ".fasta"
	resp = get(url)
	# print(resp.text[:500])
	seq = ''.join(resp.text.split('\n')[1:])
	# print(seq)
	motifs = []
	for i in range(len(seq)-3):
		if seq[i] == "N":
			if seq[i+1] != "P":
				if seq[i+2] == "S" or seq[i+2] == "T":
					if seq[i+3] != "P":
						motifs.append(i+1)
	if len(motifs) != 0:
		print(motif)
		print(*motifs)
	return


f = open("rosalind_mprt.txt")
for line in f.readlines():
	mprt(line.strip('\n'))