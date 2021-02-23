"""
Given: A positive integer n<=10^3 and an array A[1,...,n] of integers.

Return: The number of swaps performed by insertion sort algorithm on A[1,...,n].
"""

def ins(xs):
	swaps = 0
	for i in range(1,len(xs)):
		k = i
		while k>0 and xs[k]<xs[k-1]:
			xs[k], xs[k-1] = xs[k-1], xs[k]
			swaps += 1
			k -= 1
	return swaps

f = open("rosalind_ins.txt","r")
f.readline()
xs = [int(x) for x in f.readline().strip('\n').split(" ")]

print(ins(xs))