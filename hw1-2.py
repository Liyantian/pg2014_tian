def integrate(f,dx=1.0):
	i=0
	c=0
	n=len(f)
	while i<n:
		if i==0 or i==n-1:
			c=c+dx/2.0*f[i]	
		else:
			c=c+dx*f[i]
		i=i+1
	print c
f=[1.0, 3.0, 4.0, 5.0]
integrate(f)
integrate(f,0.5)
raw_input()
		

	