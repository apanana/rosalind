"""
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

f = open("rosalind_rna.txt","r")
x = f.readline()
print(x.replace("T","U"))

