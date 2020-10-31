def solve(A,K,N):
    ans=0
    cur = 0
    for i in xrange(N-1,-1,-1):
        if A[i] == cur+1:
            cur+=1
        else:
            if cur>=K: ans+=1
            if A[i] == 1:
                cur = 1
            else:
                cur = 0
    if cur>=K: ans+=1            
    return ans

t = int(raw_input())
for i in xrange(0,t):
    N,K = map(int,raw_input().split(" "))
    A = map(int,raw_input().split(" "))
    print "Case #%s: %s" %(i+1,solve(A,K,N)) 
