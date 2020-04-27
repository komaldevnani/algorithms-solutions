def start_day(on_days,D,n):
	f=D
	for i in xrange(n-1,-1,-1):
		xi = on_days[i]
		if D/xi * xi > f:
			f = f/xi * xi
		else:
			f = D/xi * xi
	return f
			

t = int(raw_input())
for i in xrange(0,t):
    n, D = map(int,raw_input().split(" "))
    on_days = map(int,raw_input().split(" "))
    print "Case #%s: %s" %(i+1,start_day(on_days, D, n))
