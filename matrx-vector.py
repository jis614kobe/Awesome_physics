def multiply(M,V):
	m = len(M)
	n = len(V)
	j=0
	l = []
	while j<m:
		i = 0
		while i<n:
			h = M[j][i] * V[i]
			l.append(h)
			i += 1
		j += 1
	w = 0
	q = 0
	answer = []
	while w < len(l):
		w += n
		s = 0
		for k in l[q:w]:
			s += k
		q += n
		answer.append(s)
	return answer

m_1 = [[2,1,2],[3,2,3],[4,1,1]]
n_1 = [1,0,1]

print multiply(m_1,n_1)