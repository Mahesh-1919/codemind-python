def am(n,m):
	c=0
	d=0
	for i in range(1,n+1):
		if n%i==0:
			c+=i
	for j in range(1,m+1):
		if m%j==0:
			d+=j
			
	if c==d:
		print('Amicable')
	else:
		print('Not Amicable')
n=int(input())
m=int(input())
am(n,m)