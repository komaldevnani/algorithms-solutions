import operator

def find_order(N,X,A):
    turns = {}
  
    for i in xrange(0, N):
        turns[i] = (A[i] + X-1) / X
                
    sorted_x = sorted(turns.items(), key=operator.itemgetter(1))
    order = [tuple[0]+1 for tuple in sorted_x]
    return order
    
t = int(raw_input())
for i in xrange(0,t):
    N,X = map(int,raw_input().split(" "))
    A = map(int,raw_input().split(" "))
    order = find_order(N,X,A)
    order = ' '.join(str(o) for o in order)
    print "Case %s: %s" %(i+1,order)
