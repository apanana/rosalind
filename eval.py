"""
Given: A positive integer n (n<=1,000,000), a DNA string s of even length at
most 10, and an array A of length at most 20, containing numbers between 0 and
1.

Return: An array B having the same length as A in which B[i] represents the
expected number of times that s will appear as a substring of a random DNA
string t of length n, where t is formed with GC-content A[i] (see "Introduction
to Random Strings").
"""
# from Decimal import 
# Decimal(str(16.2)).quantize(Decimal('.01'), rounding=ROUND_UP)
from decimal import Decimal, ROUND_UP

def eva(n,s,As):
	ys = []
	for gc in As:
		# prob of s with A[i] gc content
		conv = {"A":(1.-gc)/2.,
			"T":(1.-gc)/2.,
			"C":gc/2.,
			"G":gc/2.,}
		p = 1
		for ch in s:
			p *= conv[ch]

		# starting at i=[0,len(s)], try slotting as many s's as possible into n
		y = 0
		for i in range(len(s)):
			y += (n-i)//len(s) * p

		# needed some more accurate rounding
		y = Decimal(str(y)).quantize(Decimal('.001'), rounding=ROUND_UP)
		ys.append(y)

	return ys

f = open("rosalind_eval.txt","r")
n = int(f.readline().strip('\n'))
s = f.readline().strip('\n')
As = [float(x) for x in f.readline().split(" ")]

print(*eva(n,s,As), sep=" ")
