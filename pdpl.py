"""
Given: A multiset L containing (nC2) positive integers for some positive integer
n.

Return: A set X containing n nonnegative integers such that D(X)=L.
"""


"""
Given that the size of L is nC2, We know that n!/(2!*(n-2)!) = |L|
So |L|*2! = n(n-1)
n = (1 +- sqrt(1+4*1*|L|2!))/2a
n = (1 + sqrt(1+8|L|))2
L = 1+2+3+4+...
--------------------
A given L has multiple X that could have deltaX = L
eg:
L = {2,3,5}
S1 = {2,4,7}
S2 = {0,2,5}

--------------------
We can always assume 0 and the largest element x of L are in X.
If zero is in the set, there can't be a y > x in the set, because then
we'd need y-0 to be in L, which would mean y in L. But that's a contradiction
since x is the largest element in L.

--------------------
?? not sure if this is correct
Let Xi be last element that was added to X where we build up X from smallest
to largest elements.
Xi+1 - Xi >= Xi
If it was smaller than Xi, then (Xi+1-Xi) would be in L

No it's wrong - confusing X with L
Xi+1-Xi can be in L and not in X
-------------------
general idea:

S = [0,largest element in L]
remove largest element from L
iterate over L:
	d = diffs betwen l and S
	if diffs are a subset of L:
		add l to S
		

Q: is diffs being a subset of L_remaining sufficient to show l in S?
-> after testing this, answer is no
i guess the counterexample would be
[2,2,3,3,4,5,6,7,8,10], 3,7 would be subset of L but not in S
though I'm not sure if that still holds given that we add 2,8 first

-> other issue is that multiple candidates are possible
(i.e. mutliple elements where delta(l,S) is subset of L_remaining)
-----------------
backtracking:
could test if each element is on right or left side

test until we hit a rut, then backtrack and try again
would work but who knows how fast it is?


"""
# from collections import OrderedDict 
from math import sqrt

def make_multiset(xs):
	ms = {}
	for x in xs:
		ms.setdefault(x,0)
		ms[x] += 1
	return ms


def minkowski_diff(xs):
	ms = {}
	for x in xs:
		for y in xs:
			if x == y:
				continue
			ms.setdefault(x-y,0)
			ms[x-y] += 1
	return ms

def delta_set(xs):
	ms = {}
	for x in xs:
		for y in xs:
			if x == y or x-y < 0:
				continue
			ms.setdefault(x-y,0)
			ms[x-y] += 1
	return ms

def get_diffs(x,ys):
	ms = {}
	for y in ys:
		if x > y:
			ms.setdefault(x-y,0)
			ms[x-y] += 1
		elif x < y:
			ms.setdefault(y-x,0)
			ms[y-x] += 1
		else:
			print("this shouldnt happen??")
			print(x,y,ys)
	return ms

def is_subset(xs,ys):
	for k,v in xs.items():
		if k not in ys:
			return False
		else:
			if xs[k] > ys[k]:
				return False
	return True

def remove_subset(xs,ys):
	# assumes xs is a subset of ys
	for k,v in xs.items():
		if ys[k] == v:
			del ys[k]
		else:
			ys[k] -= v

def add_multisets(xs,ys):
	for k,v in xs.items():
		ys.setdefault(k,0)
		ys[k] += v

def max_element(xs):
	m = 0
	for k in xs.keys():
		if k > m:
			m = k
	return m

def pdpl_help(xs,ys,w):
	if len(xs) == 0:
		return ys

	x = max_element(xs)
	diffs = get_diffs(x,make_multiset(ys))
	if is_subset(diffs,xs):
		ys.setdefault(x,0)
		ys[x] += 1
		remove_subset(diffs,xs)
		ret = pdpl_help(xs,ys,w)
		if ret != None:
			return ret
		else:
			ys[x] -= 1
			if ys[x] == 0:
				del ys[x]
			add_multisets(diffs,xs)
	diffs = get_diffs(w-x,make_multiset(ys))
	if is_subset(diffs,xs):
		ys.setdefault(w-x,0)
		ys[w-x] += 1
		remove_subset(diffs,xs)
		ret = pdpl_help(xs,ys,w)
		if ret != None:
			return ret
		else:
			ys[w-x] -= 1
			if ys[w-x] == 0:
				del ys[w-x]
			add_multisets(diffs,xs)
	return None

def pdpl(xs):
	# xs is a sorted multiset in list form
	w = xs[-1]
	ys = [0,w]
	xs.remove(w)
	xs = make_multiset(xs)
	ys = make_multiset(ys)
	S = pdpl_help(xs,ys,w)
	ks = list(S.keys())
	ks.sort()
	return ks

def pdpl2(xs):
	ys = [0,xs[-1]]
	count_xs = make_multiset(xs[:-1])
	xs.remove(xs[-1])
	while xs != []:
		l = len(xs)
		candidates = []
		for x in xs:
			if x in ys:
				continue
			diff_ms = get_diffs(x,make_multiset(ys))
			
			if is_subset(diff_ms,count_xs):
				# print("subset found. x=",x)
				# print(ys)
				candidates.append(x)
				continue
				ys.insert(-1,x)
				for k,v in diff_ms.items():
					# print("k=",k,"v=",v)
					# print(count_xs)
					if count_xs[k] == v:
						# print("deleted")
						del count_xs[k]
					else:
						if count_xs[k] < v:
							print("something went wrong here")
						else:
							# print("count_xs[k]=",count_xs[k])
							count_xs[k] -= v
					for i in range(v):
						xs.remove(k)
				break
		# print("iter done")
		print("len(xs): ",len(xs)," len(ys): ",len(ys))
		print()
		# check if stuck
		if len(xs) == l:
			print("no match found")
			# print(candidates)
			# print(len(candidates))
			# cs2 = candidates.copy()
			# for c in candidates:
			# 	if c in candidates:
			# 		print(c,98961-c)
			# 		if c not in cs2:
			# 			print(candidates.index(c))
			# 		cs2.remove(c)
			# 		if (98961-c) in cs2:
			# 			cs2.remove(98961-c)
			# 		else:
			# 			print("solo")
			# 			print(c)
			# print(cs2)



			# print("xs:",xs)
			return ys

	return ys

f = open("rosalind_pdpl.txt","r")
xs = [int(x) for x in f.readline().split(" ")]
xs.sort()

# test some stuff out
# print(len(xs))
# print((1 + sqrt(1+8*len(xs)))/2)

# print(xs)
# print(make_multiset(xs))
# print(minkowski_diff(set({2,4,7})))
# print(delta_set(set({2,4,7})))
# print(delta_set(set({0,2,5})))
# print(is_subset(delta_set(set({2,4,7})), minkowski_diff(set({2,4,7}))))

# print(delta_set(set({0,3,6,8,10})))
# print(delta_set(set({0,2,4,7,10})))

# print(*pdpl([2,2,3,3,4,5,6,7,8,10]),sep=" ")
print(*pdpl(xs),sep=" ")
