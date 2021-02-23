"""
Given: Two positive integers n<=10^5 and m<=10^5, a sorted array A[1...n] of
integers from -10^5 to 10^5 and a list of m integers -10^5<=k1,...km<10^5.

Return: For each ki, output an index 1<=j<=n s.t. A[j]=ki or "-1" if there is no
such index.

"""

def bins(xs, y):
	l = 0
	r = len(xs)
	while l != r:
		i = (l + r)//2
		if len(xs[l:r]) == 1 and y != xs[i]:
			return -1
		if y == xs[i]:
			return i+1 # for some reason they index from 1
		else:
			if y < xs[i]:
				r = i
			else:
				l = i
	return -1


f = open("rosalind_bins.txt","r")
# n = int(f.readline().strip('\n'))
# m = int(f.readline().strip('\n'))
f.readline()
f.readline()
xs = [int(x) for x in f.readline().strip('\n').split(" ")]
ys = [int(y) for y in f.readline().strip('\n').split(" ")]

zs = []
for y in ys:
	zs.append(bins(xs,y))

print(*zs, sep=" ")