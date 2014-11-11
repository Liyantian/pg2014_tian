#Liyan Tian
#2014-11-04
#Homework4: Plot Sea Surface Elevation in a 1D channel

import numpy as np
import matplotlib.pyplot as plt

class SSE(object):
	
	def __init__(self, nt, dx=100.0, dt=5.0, H=10.0, g=9.8):#define the function about the sea surface elevation
		u=np.zeros(nt)    
		eta=np.ones(nt-1)
		eta[0]=3.0
		
		for t in range(0, nt-1):
			u[1:-1]=u[1:-1]-(dt*g/dx)*(eta[1:]-eta[:-1])
			eta[:]=eta[:]-(dt*H/dx)*(u[1:]-u[:-1])
		print eta
		
		x=range(0,nt-1)
		plt.plot(x,eta)
		plt.title('Sea Surface Elevation [m]', fontsize=32)
		plt.xlabel('t [s]', fontsize=20)
		plt.ylabel('eta [m]', fontsize=20)
		plt.show()
		
if __name__ == '__main__':	
	y=SSE(nt=40,)   # test the sea surface function, result should be the distribution of eta in a 1D channel 



