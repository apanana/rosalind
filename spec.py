"""
Given: A list L of n (n<=100) positive real numbers.

Return: A protein string of length n-1 whose prefix spectrum is equal to L (if
multiple solutions exist, you may output any one of them). Consult the
monoisotopic mass table.
"""

# precision too high T_T
# weights = {
# 	71.03711: "A",
# 	103.00919: "C",
# 	115.02694: "D",
# 	129.04259: "E",
# 	147.06841: "F",
# 	57.02146: "G",
# 	137.05891: "H",
# 	113.08406: "I",
# 	128.09496: "K",
# 	113.08406: "L",
# 	131.04049: "M",
# 	114.04293: "N",
# 	97.05276: "P",
# 	128.05858: "Q",
# 	156.10111: "R",
# 	87.03203: "S",
# 	101.04768: "T",
# 	99.06841: "V",
# 	186.07931: "W",
# 	163.06333: "Y", 
# }

# 4dp precision
weights = {
	71.0371: "A",
	103.0092: "C",
	115.0269: "D",
	129.0426: "E",
	147.0684: "F",
	57.0215: "G",
	137.0589: "H",
	113.0841: "I",
	128.0950: "K",
	113.0840: "L",
	131.0405: "M",
	114.0429: "N",
	97.0528: "P",
	128.0586: "Q",
	156.1011: "R",
	87.0320: "S",
	101.0477: "T",
	99.0684: "V",
	186.0793: "W",
	163.0633: "Y", 
}

def spec(ws):
	ps = ""
	for i in range(len(ws)-1):
		ps += weights[round(ws[i+1]-ws[i],4)]
	return ps

f = open("rosalind_spec.txt","r")
ws = []
for line in f.readlines():
	ws.append(float(line.strip('\n')))
print(spec(ws))
