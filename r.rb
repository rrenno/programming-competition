f,j=lambda l:[i for s in l for i in s],lambda k:ast.literal_eval(sys.argv[k])
p,d=[1, 1, 3, 3, 6, 4, 7],[[1, 4], [6, 7]]
b=[[] for i in range(len(d))]
g=f([[i for i,e in enumerate(d) if q in range(e[0],e[1]+1)] for q in p])
for i,q1 in enumerate(p):
	b[g[i]].append(q1)
print f(b)