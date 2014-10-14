#Liyan Tian
#10/14/2014
#Homework 2
#Question3:Create a 'high-pass' filter function that removes a trend from a given series of points
#using a polynomial fit of order N (specified as a functional input, default is N=1 for a
#linear fit). The function returns the difference between the given series and the polynomial
#fit.

import numpy as np
import matplotlib.pyplot as plt
def highPass(xa,ya,N=1):
	sol=np.polyfit(xa,ya,N)
	y1=np.polyval(sol,xa)
	y1=ya-y1
	return y1
if __name__ == '__main__':
	x=[1,2,3,4,5]
	y=[2,4,10,16,26]
	plt.plot(x, y, 'go')
	y2=highPass(x,y,2)
	plt.plot(x, y2, 'ro')
	plt.axis([0, 6, -2, 28])
	plt.show()
	
	raw_input()