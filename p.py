import sys,ast
z=lambda x,y,z:x if y else z
def d(b,h):
	k,l,m,n,o='| +_/'
	e,f,g=b
	p,s,t,u=[],g+1,g+f+2,f+1
	for i in range(h):
		p.append(z(z(l,i>u,n)*(i-g-1)+z(m,i in (0,s,t),z(k,i in range(1,s),o))+z('-',i in (0,s,t),l)*e+z(m,i in (0,s,t),z(k,i in range(1,s),o))+l*(f-z(u-i,i<u,0)-z(i-g-1,i>s,0))+z(z(k,i>u,z(o,i<u,m)),0<i<t,'')+n*(u-i)+z(n,i<u+1,l),i<g+f+3,l*(4+e+f)))
	return p[::-1]
c=ast.literal_eval(sys.argv[1])
h=3+max([b[1]+b[2] for b in c])
for r in range(h):
	print ''.join([p[r] for p in [d(b, h) for b in c]])