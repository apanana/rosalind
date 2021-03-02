"""
Given: A positive integer N<=100000, a number x between 0 and 1, and a DNA
string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as 
are constructed with GC-content x (see "Introduction to Random Strings"), then
at least one of the strings equals s. We allow for the same random string to be
created more than once.
"""

def rstr(N,gc,s):
	conv = {"A":(1.-gc)/2.,
			"T":(1.-gc)/2.,
			"C":gc/2.,
			"G":gc/2.,}
	p = 1
	for ch in s:
		p *= conv[ch]

	return (1-(1-p)**N)

f = open("rosalind_rstr.txt","r")
[N,gc] = [float(x) for x in f.readline().strip('\n').split(' ')]
s = f.readline().strip('\n')

print("{:.3f}".format(rstr(N,gc,s)))
