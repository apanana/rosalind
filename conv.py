"""
Given: Two multisets of positive real numbers S1 and S2. The size of each
multiset is at most 200.

Return: The largest multiplicity of S1(-)S2, as well as the absolute value of
the number x maximizing (S1(-)S2)(x) (you may return any such value if multiple
solutions exist).
"""

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

f = open("rosalind_conv.txt","r")
xs = [float(x) for x in f.readline().strip("\n").split(" ")]
ys = [float(y) for y in f.readline().strip("\n").split(" ")]
(mc, mv) = conv(xs,ys)
print(mc)
print(mv)
