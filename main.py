n = 10
m = ((2*n)-2)

for i in range(0, n):

    for j in range(0, 10):

        print (end='   ')

    for a in range(0, (1 + (i-1)*2)):
		m = m - 2
        print (a, end = '')

    print ('\n')
