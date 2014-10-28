#Liyan Tian
#10/20/2014
#Homework1: 
#Question1: Fibonacci numbers

class fib(object):
	
	def __init__(self,n):
		self.n=n
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

if __name__ == '__main__':
	#test of fib function
	fib(1)    #result should be [1]
	fib(2)    #result should be [1,1]
	fib(6)    #result should be [1,1,2,3,5,8]
	raw_input()
