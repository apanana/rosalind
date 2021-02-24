"""
Given: Two positive integers k (k<=7) and N (N<=2^k). In this problem, we begin
with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in
the 1st generation, each of whom has two children, and so on. Each organism
always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th
generation of Tom's family tree (don't count the Aa Bb mates at each level).
Assume that Mendel's second law holds for the factors.
"""

"""
g0: AaBb (x AaBb)
g1: 1/4 AA, 1/2 Aa, 1/4 aa x 1/4 BB, 1/2 Bb, 1/4 bb


----------
bc of mendel's 2nd law, problem simplifies to probability for Aa squared

g0 1/1 Aa {Aa} 1

g1 (Aa): 1/4 AA, 1/2 Aa, 1/4 aa   
	{(AA, AA), (AA, Aa), (AA, aa), ...} (9)

g2 (AA,AA): 1/2 AA 1/2 Aa *2, 1/2 AA 1/2 Aa *2  
(AA, Aa): 1/2 AA 1/2 Aa *2, 1/4 AA, 1/2 Aa 1/4 aa *2
...
-----------
prob table
AA x Aa = 1/2 AA 1/2 Aa
Aa x Aa = 1/4 AA 1/2 Aa 1/4 aa
aa x Aa =        1/2 Aa 1/2 aa

each level, total possible kid combinations (upper bound) 3^(2^n).
too large for direct calculation...
-----------


"""

"""
found another symmetry:
Treat AA and aa the same.
Prob of AA x Aa giving Aa = 1/2, not Aa (i.e AA) = 1/2
Prob of aa x Aa giving Aa = 1/2, not Aa (i.e. aa) = 1/2
(Also recall Aa x Aa giving Aa is also 1/2)
So probability for any individual is always 1/2 !!! :D :D :D
----
Working back to AaBb, we have
P(AaBb) = 1/4, P(!AaBb) = 3/4 for any given individual :')
thank god no monte carlo <3
"""
from math import comb

def lia(k,n):
	tot = 2**k
	p = (0.75**tot)
	for i in range(1,n):
		p += (0.75**(tot-i))*(0.25**(i))*comb(tot,i)
	p = 1-p
	return round(p,3)

print(lia(6,19))
