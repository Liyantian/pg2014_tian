def fib(n):
	a=1
	b=0
	i=1
	print('['),
	while i<=n:
		c=a+b		
		print(c),
		if i<n:
			print(','),
		else:
			print(']')
		a=b
		b=c
		i=i+1

fib(1)
fib(2)
fib(6)
raw_input()
