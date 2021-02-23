"""
Given: A positive integer n<=10^5 and an array A[1...n] of integers from -10^5
to 10^5.

Return: A sorted array A[1...n].
"""

# solution from MER
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

def ms(xs):
	if len(xs) <= 1:
		return xs
	else:
		return mer(ms(xs[:len(xs)//2]),
					ms(xs[len(xs)//2:]))

f = open("rosalind_ms.txt","r")
f.readline()
xs = [int(x) for x in f.readline().strip('\n').split(" ")]

zs = ms(xs)
print(*zs, sep=" ")
