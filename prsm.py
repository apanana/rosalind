"""
Given: A positive integer n followed by a collection of n protein strings
(s1, s2, ..., sn) and a multiset R of positive numbers (corresponding to the
complete spectrum of some unknown protein string).

Return: The maximum multiplicity of R(-)S[sk] taken over all strings sk, followed
by the string sk for which this maximum multiplicity occurs (you may output any
such value if multiple solutions exist).
"""
weights = {
	"A": 71.03711,
	"C": 103.00919,
	"D": 115.02694,
	"E": 129.04259,
	"F": 147.06841,
	"G": 57.02146,
	"H": 137.05891,
	"I": 113.08406,
	"K": 128.09496,
	"L": 113.08406,
	"M": 131.04049,
	"N": 114.04293,
	"P": 97.05276,
	"Q": 128.05858,
	"R": 156.10111,
	"S": 87.03203,
	"T": 101.04768,
	"V": 99.06841,
	"W": 186.07931,
	"Y": 163.06333, 
}


# sol from CONV:
def conv(xs, ys):
	zs = {}
	for x in xs:
		for y in ys:
			diff = round(x-y,5)
			if diff in zs.keys():
				zs[diff] += 1
			else:
				zs[diff] = 1
	max_count = 0
	max_val = 0.0
	for z, c in zs.iteritems():
		if c > max_count:
			max_count = c
			max_val = z
	return (max_count,max_val)

def complete_spectrum(ps):
	front_sum = 0
	back_sum = 0
	cs = []
	for i in range(len(p)-1):
		front_sum += weights[ps[i]]
		back_sum += weights[ps[-(i+1)]]
		cs.append(front_sum)
		cs.append(back_sum)
	cs.append(front_sum + weights[ps[-1]])
	return cs


f = open("rosalind_prsm.txt","r")
n = int(f.readline().strip('\n'))

ps = []
for i in range(n):
	ps.append(f.readline().strip('\n'))

R = []
for line in f.readlines():
	R.append(float(line.strip('\n')))

# find complete spectrum for each protein
cs_dict = {}
for p in ps:
	cs_dict[p] = complete_spectrum(p)

# find multiplicity for each protein
mult_dict = {}
for p, cs in cs_dict.iteritems():
	mult_dict[p] = conv(R,cs)[0]

# find and report greatest multiplicty and corresponding protein
max_m = 0
max_p = ""
for p, m in mult_dict.iteritems():
	if m > max_m:
		max_m = m
		max_p = p
print(max_m)
print(max_p)
