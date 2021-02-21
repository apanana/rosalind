"""
Given: Three positive integers k, m, and n, representing a population containing
k+m+n organisms: k individuals are homozygous dominant for a factor, m are 
heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce
an individual possessing a dominant allele (and thus displaying the dominant
phenotype). Assume that any two organisms can mate.
"""
from __future__ import division

def iprb(k,m,n):
	t = k+m+n
	kk = (k / t) * ((k-1) / (t-1))
	km = (k / t) * (m / (t-1)) * 2
	kn = (k / t) * (n / (t-1)) * 2
	mm = (m / t) * ((m-1) / (t-1)) * (3 / 4)
	mn = (m / t) * (n / (t-1))
	return kk + km + kn + mm + mn

# print iprb(2,2,2)
print iprb(15,18,30)