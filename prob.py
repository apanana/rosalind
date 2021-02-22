"""
Given: A DNA string s of length at most 100 bp and an array A containing at most
20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the
common logarithm of the probability that a random string constructed with the
GC-content found in A[k] will match s exactly.
"""
import math

def prob(s, gcs):
	ls = []
	for gc in gcs:
		conv = {"A":(1.-gc)/2.,
			"T":(1.-gc)/2.,
			"C":gc/2.,
			"G":gc/2.,}
		l = 0
		for ch in s:
			l += math.log(conv[ch],10) # more accurate fp number at the end
		ls.append("{:.3f}".format(l))
	print(*ls, sep=" ")

# prob("ACGATACAA",[0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783])

f = open("rosalind_prob.txt","r")
s = f.readline().strip('\n')
gcs_raw = f.readline().strip('\n')
gcs = [float(gc) for gc in gcs_raw.split(" ")]
prob(s,gcs)