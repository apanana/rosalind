"""
Given: A multiset L containing (nC2) positive integers for some positive integer
n.

Return: A set X containing n nonnegative integers such that D(X)=L.
"""

def pdpl(xs):
	print(xs)
	ys = [0]
	for x in xs:
		print(x,ys)
		if x not in ys:
			ys.append(ys[-1]+x)
	return ys

f = open("rosalind_pdpl.txt","r")
xs = [int(x) for x in f.readline().split(" ")]
print(*pdpl(xs),sep=" ")