"""
Given: Positive integers n<=100 and m<=20.

Return: The total number of pairs of rabbits that will remain after the n-th
month if all rabbits live for m months.
"""

def fibd(n,m):
	a = [0,1] # adults
	b = [1,0] # born
	for i in range(2,n):
		b.append(a[i-1])
		died = b[i-m] if (i-m) >= 0 else 0
		a.append(a[i-1] + b[i-1] - died)
	return a[-1] + b[-1]

print(fibd(98,19)) #bruh... 