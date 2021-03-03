"""
Given: A positive integer n<=10000 followed by a permutation pi of length n.

Return: A longest increasing subsequence of pi, followed by a longest decreasing
subsequence of pi.
"""

def longest_inc_subseq(xs):
	# ti = (prev_index, length so far)
	t = [(-1,1)]*len(xs)
	max_len = 1
	max_i = 0
	for i in range(1,len(xs)):
		for j in range(i):
			if xs[i] > xs[j] and t[i][1] < t[j][1] + 1:
				t[i] = (j,t[j][1] + 1)
				if t[i][1] > max_len:
					max_len = t[i][1]
					max_i = i
	ys = []
	while max_i != -1:
		ys.append(xs[max_i])
		max_i = t[max_i][0]
	ys.reverse()
	return ys

def longest_dec_subseq(xs):
	# ti = (prev_index, length so far)
	t = [(-1,1)]*len(xs)
	max_len = 1
	max_i = 0
	for i in range(1,len(xs)):
		for j in range(i):
			if xs[i] < xs[j] and t[i][1] < t[j][1] + 1:
				t[i] = (j,t[j][1] + 1)
				if t[i][1] > max_len:
					max_len = t[i][1]
					max_i = i
	ys = []
	while max_i != -1:
		ys.append(xs[max_i])
		max_i = t[max_i][0]
	ys.reverse()
	return ys

# print(longest_inc_subseq([5,1,4,2,3]))
# print(longest_dec_subseq([5,1,4,2,3]))


f = open("rosalind_lgis.txt","r")
f.readline()
xs = [int(x) for x in f.readline().strip('\n').split(" ")]

print(*longest_inc_subseq(xs), sep=" ")
print(*longest_dec_subseq(xs), sep=" ")


