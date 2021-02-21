"""
Given: Six nonnegative integers, each of which does not exceed 20,000. 
The integers correspond to the number of couples in a population possessing 
each genotype pairing for a given factor. In order, the six given integers 
represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in 
the next generation, under the assumption that every couple has exactly two 
offspring.
"""

def iev(dd, dh, dr, hh, hr, rr):
	# expected offspring for each type
	dde = 2
	dhe = 2
	dre = 2
	hhe = 3.0/4 * 2
	hre = 0.5 * 2
	rre = 0
	print(dd*dde, dh*dhe, dr*dre, hh*hhe, hr*hre, rr*rre)
	total = dd*dde + dh*dhe + dr*dre + hh*hhe + hr*hre + rr*rre
	return total

print(iev(1,0,0,1,0,1))

print(iev(17457,19013,19576,19636,16590,19787))

