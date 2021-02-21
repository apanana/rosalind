"""
Given: Positive integers n<=40 and k<=5.

Return: The total number of rabbit pairs that will be present after n months, 
if we begin with 1 pair and in each generation, every pair of reproduction-age 
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

def fib(n,k):
	rabbits = [0]*40
	rabbits[0] = 1
	rabbits[1] = 1
	i = 2
	while i < n:
		rabbits[i] = rabbits[i-1] + rabbits[i-2]*k
		i+=1
	return rabbits[i-1]

print(fib(31,2))
