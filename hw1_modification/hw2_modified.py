#Liyan Tian
#10/20/2014
#Homework1: 
#Question2: integral of a list of numbers
import numpy as np
class integrate(object):
	
	def __init__(self,f,dx=1.0):
		print (f.sum()+f[1:-1].sum())*dx/2
		
if __name__ == '__main__':
	#test of integrate function
	f=np.array([1.0, 3.0, 4.0, 5.0])
	integrate(f)    #result should be 10.0
	integrate(f,0.5)    #result should be 5.0
	
raw_input()

	