ss = list('INSERTIONSORT')

def insertion_sort(ss):
	for i in xrange(1,len(ss)):		
		j = i
		while j > 0 and ss[j] < ss[j - 1]:
			ss[j],ss[j - 1] = ss[j - 1], ss[j]
			j -= 1

		print ''.join(ss[0:i] + list('|') + ss[i:len(ss)])
    
	print '\nResult: ' + ''.join(ss)	

insertion_sort(ss)