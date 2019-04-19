def traverse_postorder(nodes, children, visit):
    info = {n: -1 for n in nodes}
    stack = []
    for node in nodes:
        if info[node] == -1:
            stack.append(node)
            while stack:
                nd = stack.pop()
                if info[nd] == -1:
                    info[nd] = -2
                    stack.append(nd)
                    stack.extend(ch for ch in children(nd) if info[ch] == -1)
                elif info[nd] == -2:
                    visit(nd, info)
    return info

def main():
    N = 15
    MOVES = [(-2, 1), (-2, -1), (1, -2), (-1, -2)]
    
    def nim_sum(a): return reduce(lambda x, y: x ^ y, a, 0)
    
    def mex(a):
        s = set(a)
        n = len(s)
        for i in xrange(n):
            if not i in s:
                return i
        return n

    my_nodes = [(r, c) for r in xrange(N) for c in xrange(N)]

    def inside(rc):
        r, c = rc
        return r >= 0 and r < N and c >= 0 and c < N

    def children(node):
        r, c = node
        return filter(inside, ((r+y, c+x) for x, y in MOVES))
        
    def visit(node, info):
        info[node] = mex(info[ch] for ch in children(node))
        
    sg = traverse_postorder(my_nodes, children, visit)

    for _ in xrange(input()):
        k = input()
        rc = [map(int, raw_input().split()) for _i in xrange(k)]
        result = nim_sum(sg[r-1, c-1] for r, c in rc)
        print ("First", "Second")[result==0]

main()
