x=int(input('enter '))
l=[1,1]
if x==1:
	print('1')
elif x==2:
	print('1')
else:
	for a in range(2,x):
		b=l[a-2]+l[a-1]
		l.append(b)
	print(l[-1])
