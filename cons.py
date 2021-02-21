"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in
FASTA format.

Return: A consensus string and profile matrix for the collection. (If several 
possible consensus strings exist, then you may return any one of them.)
"""
# counts is an array of arrays of length 4
# each length 4 array corresponds to [A,C,G,T] for a given column
counts = [] 
conv = dict([(y,x) for x,y in enumerate("ACGT")])

f = open("rosalind_cons.txt","r")
last_seq = ""
for line in f.readlines():
	if line[0] == ">":
		# skip first ">" line:
		if last_seq == "":
			continue
		else:
			# establish array
			if len(counts) == 0:
				counts = [[0,0,0,0] for x in range(len(last_seq))]
			# update counts
			for i in range(len(last_seq)):
				counts[i][conv[last_seq[i]]] += 1
			# clear our string
			last_seq = ""
			continue
	else:
		# add to our string
		last_seq += line.strip('\n')

# process last seq since we aren't triggered again by a ">"
# update counts
for i in range(len(last_seq)):
	counts[i][conv[last_seq[i]]] += 1

# create the consensus. there may be multiple, but we don't care about which one
consensus = ""
for count in counts:
	consensus += "ACGT"[count.index(max(count))]

print(consensus)

for base in "ACGT":
	print(base + ":", end ="")
	for count in counts:
		print(" " + str(count[conv[base]]), end ="")
	print()
