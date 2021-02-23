"""
Given: A positive integer n<=10^5 and a sorted array A[1...n] of integers from
-10^5 to 10^5, a positive integer m<=10^5 and a sorted array B[1...m] of
integers from -10^5 to 10^5.

Return: A sorted array C[1...n+m] containing all the elements of A and B.
"""

def mer(xs,ys):
	zs = []
	i,j = 0,0
	while i < len(xs) and j < len(ys):
		if xs[i] < ys[j]:
			zs.append(xs[i])
			i += 1
		else:
			zs.append(ys[j])
			j += 1
	# fill remainder
	zs += xs[i:]
	zs += ys[j:]
	return zs

f = open("rosalind_mer.txt","r")
f.readline()
xs = [int(x) for x in f.readline().strip('\n').split(" ")]
f.readline()
ys = [int(y) for y in f.readline().strip('\n').split(" ")]

zs = mer(xs,ys)
print(*zs, sep=" ")
