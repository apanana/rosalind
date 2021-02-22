"""
Given: A list L containing 2n+3 positive real numbers (n<=100). The first number
in L is the parent mass of a peptide P, and all other numbers represent the
masses of some b-ions and y-ions of P (in no particular order). You may assume
that if the mass of a b-ion is present, then so is that of its complementary
y-ion, and vice-versa.

Return: A protein string t of length n for which there exist two positive real
numbers w1 and w2 such that for every prefix p and suffix s of t, each of
w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists a
protein string whose t-prefix and t-suffix weights correspond to the non-parent
mass values of L.) If multiple solutions exist, you may output any one.
"""

# solution from SPEC
weights = {
	71.03711: "A",
	103.00919: "C",
	115.02694: "D",
	129.04259: "E",
	147.06841: "F",
	57.02146: "G",
	137.05891: "H",
	113.08406: "I",
	128.09496: "K",
	113.08406: "L",
	131.04049: "M",
	114.04293: "N",
	97.05276: "P",
	128.05858: "Q",
	156.10111: "R",
	87.03203: "S",
	101.04768: "T",
	99.06841: "V",
	186.07931: "W",
	163.06333: "Y", 
}

def spec(ws):
	ps = ""
	for i in range(len(ws) - 1):
		ps += weights[round(ws[i+1] - ws[i], 5)]
	return ps

def full(L):
	# assume L is [P] + a sorted list of [b-ions and y-ions]
	bs_l = [L[1]]
	bs_r = []
	P = L[0]
	for i in range(2, len(L)/2+1):
		diff = round(L[i] - bs_l[-1], 5)
		if diff in weights.keys():
			bs_l.append(L[i])
		else:
			bs_r.append(L[-i])
	bs = bs_l + bs_r
	bs.sort()
	return spec(bs)

f = open("rosalind_full.txt","r")
L = []
for line in f.readlines():
	L.append(float(line.strip('\n')))

print(full(L))
