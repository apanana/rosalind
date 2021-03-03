"""
Given: A collection of at most 5 pairs of permutations, all of which have length
10.

Return: The reversal distance between each permutation pair.
"""
import itertools as it
from math import factorial
from ast import literal_eval

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

###########
# N = 9

# ## make nodes
# PS = list(it.permutations(range(1,N+1)))
# PS_index = {k:v for v,k in enumerate(PS)}

## make edges
# edges = []
# e_count = 0
# for i in range(len(PS)):
# 	e = []
# 	# if i % 100000 == 0:
# 	# 	print(i)
# 	# 	print(e_count)
# 	for j in range(N-1):
# 		for k in range(j+1,N):
# 			t = list(PS[i])
# 			t[j],t[k] = t[k], t[j]
# 			e.append(PS_index[tuple(t)])
# 			# e.append(perm_index(t))
# 			# e.append(PS.index(tuple(t)))
# 			e_count += 1
# 	edges.append(e)
# # print(edges)
# # for i in range(len(PS)):
# # 	print(PS[i],edges[i])
# for edge in edges:
# 	print(*edge, sep=",")
# print("DONE")

## edges from file
# f = open("edges10.txt","r")
# read_edges = []
# i = 0
# for line in f.readlines():
# 	if i % 100000 == 0:
# 		print(i)
# 	read_edges.append([int(x) for x in line.strip('\n').split(" ")])
# 	i += 1
# print("DONE")

# f = open("edges.txt","r")
# edges = [list(literal_eval(line)) for line in f]
# for edge in edges:
# 	print(*edge, sep=" ")

# check
# print(edges == read_edges)

####
def rear2(p1, p2):
	# bfs of all reverals
	visited = {}
	for p in PS:
		visited[p] = -1
	visited[p1] = 0
	to_visit = [p1]
	parent = {}
	for p in PS:
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
		# adj = perm_reversals(to_visit[0])
		# adj = [PS_index[x] for x in adj]
		# for i in adj:
		for i in edges[PS_index[to_visit[0]]]:
			if visited[PS[i]] == -1:
				visited[PS[i]] = visited[to_visit[0]]+1
				to_visit.append(PS[i])
				parent[PS[i]] = to_visit[0]
		to_visit.remove(to_visit[0])
	return -1, None

def rear(p1, p2):
	# bfs of all reverals
	visited = {p1:0}
	to_visit = [p1]
	parent = {p1:None}
	while len(to_visit) != 0:
		curr = to_visit[0]
		if curr == p2:
			# return once we find our node
			
			path = []
			while curr != None:
				path.append(curr)
				curr = parent[curr]
			path.reverse()
			return visited[to_visit[0]], path
		edges = []
		for i in range(len(curr)-1):
			for j in range(i+1,len(curr)):
				next = list(curr)
				next[i], next[j] = next[j], next[i]
				next = tuple(next)
				if next not in visited:
					visited[next] = visited[curr]+1
					parent[next] = curr
					to_visit.append(next)

		# for i in edges[PS_index[to_visit[0]]]:
		# 	if visited[PS[i]] == -1:
		# 		visited[PS[i]] = visited[to_visit[0]]+1
		# 		to_visit.append(PS[i])
		# 		parent[PS[i]] = to_visit[0]
		to_visit.remove(curr)
	return -1, None


# for i in range(len(PS)):
# 	e = []
# 	for j in range(N-1):
# 		for k in range(j+1,N):
# 			t = list(PS[i])
# 			t[j],t[k] = t[k], t[j]
# 			e.append(PS_index[tuple(t)])
# 	edges.append(e)
# print(edges)
# for i in range(len(PS)):
# 	print(PS[i],edges[i])
# for edge in edges:
# 	print(*edge, sep=",")
# print("DONE")


# p1 = (1,2,3,4,5)
# p2 = (3,1,5,4,2)
# print(rear(p1,p2))

p1 = (1,2,3,4,5,6,7,8,9)
p2 = (9,1,2,3,4,5,6,7,8)
print(rear(p1,p2))

# p1 = (1,2,3,4,5,6,7,8,9,10)
# p2 = (3,1,5,2,7,4,9,6,10,8)
# print(rear(p1,p2))


# f = open("rosalind_rear.txt","r")
# rs = []
# p1 = []
# p2 = []
# for line in f.readlines():
# 	if line == "\n":
# 		rs.append(rear(tuple(p1),tuple(p2)))
# 		p1 = []
# 		p2 = []
# 	if p1 == []:
# 		p1 = [int(x) for x in line.strip('\n').split(" ")]
# 	else:
# 		p2 = [int(x) for x in line.strip('\n').split(" ")]
# rs.append(rear(tuple(p1),tuple(p2)))

# print(*rs, sep=" ")
