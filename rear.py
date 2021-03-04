"""
Given: A collection of at most 5 pairs of permutations, all of which have length
10.

Return: The reversal distance between each permutation pair.
"""
from collections import deque

def rear(p1, p2):
	# bfs of all reverals
	visited = {p1: 0}
	# parent = {p1: None} # for reconstructing the path
	to_visit = deque([p1])
	searched = 0
	while len(to_visit) != 0:
		curr = to_visit.popleft()
		for i in range(len(curr)-1):
			for j in range(i+1,len(curr)):
				next = list(curr)
				next[i], next[j] = next[j], next[i]
				next = tuple(next)
				if next == p2: # return once we find our node
					return visited[curr]+1
					# l = visited[curr]+1
					# path = [next]
					# while curr != None:
					# 	path.append(curr)
					# 	curr = parent[curr]
					# path.reverse()
					# return l, path
				if next not in visited:
					visited[next] = visited[curr]+1
					# parent[next] = curr
					to_visit.append(next)
				if next in visited:
					if visited[next] > visited[curr] + 1:
						print("wtf?")
						print(curr,next)
						return -1
						# visited[next] = visited[curr] + 1
		searched += 1
		if searched % 100000 == 0:
			print(searched)
	# return -1, None
	return -1

# p1 = (1,2,3,4,5)
# p2 = (3,1,5,4,2)
# print(rear(p1,p2))

# p1 = (1,2,3,4,5,6,7,8,9)
# p2 = (9,1,2,3,4,5,6,7,8)
# print(rear(p1,p2))

# p1 = (1,2,3,4,5,6,7,8,9,10)
# p2 = (3,1,5,2,7,4,9,6,10,8)
# print(rear(p1,p2))

p1 = (3, 10, 8, 2, 5, 4, 7, 1, 6, 9)
p2 = (5, 2, 3, 1, 7, 4, 10, 8, 6, 9)
print(rear(p1,p2))

# (8 6 7 9 4 1 3 10 2 5)
# (8 2 7 6 9 1 5 3 10 4)


# f = open("rosalind_rear.txt","r")
# rs = []
# p1 = []
# p2 = []
# for line in f.readlines():
# 	if line == "\n":
# 		rs.append(rear(p1,p2))
# 		p1 = []
# 		p2 = []
# 		continue
# 	if p1 == []:
# 		p1 = tuple([int(x) for x in line.strip('\n').split(" ")])
# 	else:
# 		p2 = tuple([int(x) for x in line.strip('\n').split(" ")])
# rs.append(rear(p1,p2))
# print(*rs, sep=" ")
