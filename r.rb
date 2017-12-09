import sys,ast
f = lambda l:[i for s in l for i in s]
p = ast.literal_eval(sys.argv[1])
d = ast.literal_eval(sys.argv[2])
b = [[] for i in range(len(d))]

g = f([[i for i, e in enumerate(d) if q in range(e[0],e[1]+1)] for q in p])
for i, q1 in enumerate(p):
	b[g[i]].append(q1)

print f(b)