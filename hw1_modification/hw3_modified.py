#Liyan Tian
#10/20/2014
#Homework1: 
#Question3: Read the data from the file discharge.dat, return a list of dates and discharge.

import numpy as np
import datetime

class discharge(object):

	def __init__(self, filename):
		self.filename=filename
		f=open(self.filename)
		dates=[]
		discharges=[]
		for line in f.readlines():
			if line[0]!= '#':
				data=line.split('	')
				n=len(data[3])-3
				date=data[2]
				discharge=data[3][:n]
				dates.append(date)
				discharges.append(discharge)
			
		self.date=np.array(dates)
		self.discharge=np.array(discharges)
		
		print self.date    #return a list of dates
		print self.discharge    #return a list of discharge
		
if __name__=='__main__':
	#test of discharge function
	filename='discharge.dat'
	dates1=discharge(filename)  #result should return a list of dates and discharge
	
raw_input()
	