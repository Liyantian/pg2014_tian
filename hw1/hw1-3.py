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
		
		print self.date
		print self.discharge
		
if __name__=='__main__':		
	filename='discharge.dat'
	dates1=discharge(filename)
	
raw_input()
	