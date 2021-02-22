"""
Given: A positive integer n (n<=1000).

Return: The total number of subsets of {1,2,...,n} modulo 1,000,000.
"""

def sset(n):
	prod = 1
	for i in range(n):
		prod *= 2
		prod %= 1000000
	return prod

print(sset(899))