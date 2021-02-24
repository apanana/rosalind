"""
Given: Positive integers n and k such that 100>=n>0 and 10>=k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.
"""

def pper(n,k):
	prod = 1
	for i in range(n-k+1,n+1):
		prod *= i
		prod %= 1000000
	return prod

print(pper(93,10))
