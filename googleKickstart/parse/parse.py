#The rover can be maneuvered around on the surface of the planet by sending it a program, which is a string of characters representing movements in the four cardinal directions. The robot executes each character of the string in order:
#N: Move one unit north.
#S: Move one unit south.
#E: Move one unit east.
#W: Move one unit west.
#There is also a special instruction X(Y), where X is a number between 2 and 9 inclusive and Y is a non-empty subprogram. This denotes that the robot should repeat the subprogram Y a total of X times.
#Since the planet is a torus, the first and last columns are adjacent, so moving east from column 109 will move the rover to column 1 and moving south from row 109 will move the rover to row 1. Similarly, moving west from column 1 will move the rover to column 109 and moving north from row 1 will move the rover to row 109. Given a program that the robot will execute, determine the final position of the robot after it has finished all its movements.

def final_square(s):
	i=0
	m=w=h=1
	t = []	
	while i<len(s):
		
		if s[i] == 'S':
			h = (h+m) % 1000000000

		elif s[i] == 'N':
			h = h-m
			if h <= 0:
				h = 1000000000 + h

		elif s[i] == 'E':
			w = (w+m) % 1000000000

		elif s[i] == 'W':
			w = w-m
			if w <= 0:
				w = 1000000000 + w
		
		elif s[i].isdigit():
			t.append(int(s[i]))			
			m *= int(s[i])
			i=i+1
		elif s[i] == ')':
			m /= t.pop()
			
		i+=1

	return "%s %s" %(w,h)

t= int(raw_input())
for i in xrange(0,t):
    s = raw_input()
    print "Case #%s: %s" %(i+1,final_square(s))
			
