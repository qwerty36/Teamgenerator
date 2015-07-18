from mod_python import apache
from random import shuffle

	file = open("participants.txt", 'r')
	f = file.readlines()
	names = []

	for line in f:
		names.append(line.strip())

	x = len(names)
	y = (x + 10 // 2) // 10
	print ('Number of participants')
	print (x)
	print ('\n')
	print ('Number of teams')
	print (y)
	print ('\n')
	teams = y

	shuffle(names)
	j=0
	for i in range(len(names)):
		print ('Team %i: %s'%(j%teams,names[i-1]))
		j+=1