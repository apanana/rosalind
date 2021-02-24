"""
Given: A positive integer n (n<=20,000) and two subsets A and B of {1,2,...,n}.

Return: Six sets: AUB, AnB, A-B, B-A, Ac, and Bc (where set complements are
taken with respect to {1,2,...,n}).
"""

f = open("rosalind_seto.txt","r")
U = set([x+1 for x in range(int(f.readline().strip("\n")))])
A = set([int(x) for x in f.readline().strip('\n').strip(' ')[1:-1].split(",")])
B = set([int(x) for x in f.readline().strip('\n').strip(' ')[1:-1].split(",")])


print(A|B)
print(A&B)
print(A-B)
print(B-A)
print(U-A)
print(U-B)
