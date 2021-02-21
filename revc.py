"""
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

def revc(s):
	t = ""
	for base in s:
		if base == "A":
			t += "T"
		elif base == "C":
			t += "G"
		elif base =="G":
			t += "C"
		elif base == "T":
			t += "A"
	return t[::-1]

# s = "AAAACCCGGT"
# print revc(s)

f = open("rosalind_revc.txt","r")
x = f.readline()
# print(x)
print revc(x)
