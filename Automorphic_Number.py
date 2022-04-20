def am(n):
	s=n**2
	s=str(s)
	n=str(n)
	x=len(n)
	if n==s[-x::]:
		print('Automorphic Number')
	else:
		print('Not an Automorphic Number')
n=int(input())
am(n)