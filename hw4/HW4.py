#Liyan Tian
#2014-11-04
#Homework4: Plot Sea Surface Elevation

import numpy as np
import matplotlib.pyplot as plt

def SSE(nx, nt, dx, dt, H, g=9.8):  #define the sea surface elevation function
	u=np.zeros((nx,nt))    
	eta=np.zeros((nx,nt-1))
	eta[0,0]=3.0
	
	for x in range(0, nx-1):
		u[x+1, 1:-1]=u[x, 1:-1]-g*dt/dx*(eta[x, 1:]-eta[x, :-1])
		eta[x+1, :]=eta[x, :]-H*dt/dx*(u[x+1, 1:]-u[x+1, :-1])
	
	x=range(0,nx)
	t=range(0,nt-1)
	T,X=np.meshgrid(t,x)
	
	pcm=plt.pcolor(X,T,eta,cmap=plt.cm.RdBu_r,)
	plt.title('Sea Surface Elevation [m]', fontsize=36)
	plt.xlabel('x [m]', fontsize=20)
	plt.ylabel('t [s]', fontsize=20)
	cb=plt.colorbar(pcm)
	cb.set_label('Sea Surface Elevation [m]', fontsize=24)
	
	plt.show()
	
SSE(nx=700, nt=20, dx=1000., dt=15., H=16.)   # test the sea surface elevation function, result should be a figure about the sea surface elevation