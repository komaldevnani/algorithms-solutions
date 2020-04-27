def find_peak(n,H):    
    count = 0
    for j in xrange(0,n):
    	if j > 0 and j < (n-1):
    		if H[j] > prev and H[j] > H[j+1]:
    			count +=1
    
    	prev = H[j]
    
    return count

t = int(raw_input())
for i in xrange(0,t):	
	n = int(raw_input())
	H = map(int,raw_input().split(" "))
	c=find_peak(n,H)
	print "Case %s: %s" %(i+1,c)





