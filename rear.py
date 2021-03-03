"""
Given: A collection of at most 5 pairs of permutations, all of which have length
10.

Return: The reversal distance between each permutation pair.
"""
import itertools as it
from math import factorial

# def perm_help(fixed, to_perm):
# 	# nothing left to permute
# 	if len(to_perm) == 1:
# 		return [1, [tuple(fixed+to_perm)]] # bc fuck space efficiency amirite? :D
# 	# fix one number from to_perm and permute on the remaining numbers
# 	else:
# 		records = [0, []]
# 		for i in to_perm:
# 			rec = perm_help(fixed+[i],[x for x in to_perm if x != i])
# 			records[0] += rec[0]
# 			records[1] += rec[1]
# 		return records

# def perm(n):
# 	ps = perm_help([],[i+1 for i in range(n)])
# 	return ps[1]

def perm_reversals(p):
	p_revs = []
	for i in range(len(p)-1):
		for j in range(i+1,len(p)):
			b = list(p)
			b[i],b[j] = b[j], b[i]
			p_revs.append(tuple(b))
	return p_revs



def perm_index(p):
	result = 0
	for j in range(len(p)):
		k = sum(1 for i in p[j + 1:] if i < p[j])
		result += k * factorial(len(p) - j - 1)
	return result

	# index = 0
	# for i in p[:-1]:
	# 	index += (i-1) * factorial(n-1)
	# 	n -= 1
	# return index

def rear(p1, p2):
	# bfs of all reverals
	visited = {}
	for p in ps:
		visited[p] = -1
	visited[p1] = 0
	to_visit = [p1]
	parent = {}
	for p in ps:
		parent[p] = None
	while len(to_visit) != 0:
		# print(to_visit[0])
		if to_visit[0] == p2:
			p = to_visit[0]
			path = []
			while p != None:
				path.append(p)
				p = parent[p]
			path.reverse()
			return visited[to_visit[0]], path
		for i in edges[ps.index(to_visit[0])]:
		# adj = perm_reversals(to_visit[0])
		# adj = [ps.index(x) for x in adj]
		# for i in adj:
			if visited[ps[i]] == -1:
				visited[ps[i]] = visited[to_visit[0]]+1
				to_visit.append(ps[i])
				parent[ps[i]] = to_visit[0]
		to_visit.remove(to_visit[0])
	return -1, None

n = 10
# nodes
# ps = perm(7)
ps = list(it.permutations(range(1,n+1)))
# for p in ps:
# 	print(p)
# print("len(ps)=",len(ps))
# print(ps)
print("HI")

# for p in ps:
# 	print(p,perm_index(p))

edges = []
for i in range(len(ps)):
	edges.append([])
for i in range(len(ps)):
	if i % 100 == 0:
		print(i)
	p_revs = perm_reversals(ps[i])
	for p_rev in p_revs:
		edges[i].append(perm_index(p_rev))
	# print(i,edges)

# class ehrlich_iter:
#   def __init__(self, n):
#     self.n = n
#     self.b = range(0, n)
#     self.c = [0] * (n + 1)

#   def __iter__(self):
#     return self

#   def next(self):
#     k = 1
#     while self.c[k] == k:
#       self.c[k] = 0
#       k += 1
#     if k == self.n:
#       raise StopIteration
#     self.c[k] += 1
#     self.b[1:k - 1].reverse
#     return self.b[k]

# mylist = [ 1, 2, 3, 4 ]   # test it
# print("Starting permutation: ", mylist)
# for v in ehrlich_iter(len(mylist)):
#   mylist[0], mylist[v] = mylist[v], mylist[0]
#   print("Next permutation: ", mylist)
# print("All permutations traversed.")

# edges = []
# for i in range(n):
# 	edges.append([])
# for i in range(n):
# 	if i % 100 == 0:
# 		print(i)
# 	p_revs = perm_reversals(ps[i])
# 	for p_rev in p_revs:
# 		# if ps.index(p_rev) not in edges[i]:
# 		# 	edges[i].append(ps.index(p_rev))
# 		# if i not in edges[ps.index(p_rev)]:
# 		# 	edges[ps.index(p_rev)].append(i)
# 		# ^ slower
# 		edges[i].append(ps.index(p_rev))
# 	# print(i,edges)

# print(edges)
print("HI")


# p1 = (1,2,3,4,5)
# p2 = (3,1,5,4,2)
# print(rear(p1,p2))

# p1 = (1,2,3,4,5,6,7,8,9,10)
# p2 = (3,1,5,2,7,4,9,6,10,8)
# print(rear(p1,p2))


# f = open("rosalind_rear.txt","r")

# rs = []
# p1 = []
# p2 = []
# for line in f.readlines():
# 	if line == "\n":
# 		rs.append(rear(p1,p2))
# 		p1 = []
# 		p2 = []
# 	if p1 == []:
# 		p1 = [int(x) for x in line.strip('\n').split(" ")]
# 	else:
# 		p2 = [int(x) for x in line.strip('\n').split(" ")]
# rs.append(rear(p1,p2))

# print(*rs, sep=" ")