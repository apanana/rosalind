"""
Given: Positive integers n and m with 0<=m<=n<=2000.

Return: The sum of combinations C(n,k) for all k satisfying m<=k<=n,
modulo 1,000,000. In shorthand, Sum(k=[m,n])(nk).

"""
from math import comb

def aspc(n,m):
	tot = 0
	for i in range(m,n+1):
		tot += comb(n,i)
		tot %= 1000000
	return tot

print(aspc(1892,604))
