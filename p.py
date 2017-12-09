import sys,ast
def draw_a_box(b,max_height):
	l,w,h = 0, 1, 2
	p,s,t,u = [], b[h]+1, b[h]+b[w]+2, b[w]+1

	for i in range(max_height):
		fs=(' ' if i>u else '_') * (i-b[h]-1)
		bw='+' if i in (0,s,t) else ('|' if i in range(1,s) else '/')
		bs='-' if i in (0,s,t) else ' '
		ts=' ' * (b[w] - (u-i if i<u else 0) - (i-b[h]-1 if i > s else 0))
		tss='_' * (u-i)
		tsw=('|' if i>u else ('/' if i<u else '+')) if i<t and i>0 else ''
		es='_' if i<u+1 else ' '
		p.append(fs+bw+bs*b[l]+bw+ts+tsw+tss+es if i<b[h]+b[w]+3 else ' '*(4+b[l]+b[w]))

	p.reverse()

	return p

l, w, h = 0, 1, 2
boxes = ast.literal_eval(sys.argv[1])
max_height = 3 + max([b[h] + b[w] for b in boxes])
space_bbox = (max_height, 1)
space_box_count = len(boxes) - 1
space_box_line_count = boxes[0][w] + 2
box_bbox = [(max_height, 3 + b[l] + b[w]) for b in boxes]


for r in range(max_height):
	print ''.join([p[r] for p in [draw_a_box(b, max_height) for b in boxes]])
