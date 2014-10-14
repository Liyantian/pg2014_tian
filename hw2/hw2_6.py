#Liyan Tian
#10/14/2014
#Homework 2
# 6. Continue with the class created in question 4, adding the following methods:

 # - Get a mean annual timeseries. Return the mean annual hydrograph with dates given for some
   # arbitrary (specified) year. 
 # - Create a plot of a given year with mean discharge and variability. Plot the given year as 
   # a red line. Plot the annual mean hydrograph as a black line. Plot a grey shaded region around 
   # the black line representing one standard deviation about the mean (use the plt.fill() command 
   # for this).

import numpy as np
import matplotlib.pyplot as plt
import datetime
class Data(object):
	def __init__(self,date1,data1):
		self.date=date1
		self.data=data1
		
	def __str__(self):
		return '(%s, %s)' % (self.date, self.data)
	def __repr__(self):
		return '(%s, %s)' % (self.date, self.data)

class Hydro(object):

	def __init__(self, filename):
		self.filename = filename
		self.reading = []
		f=open(self.filename)
		for line in f.readlines():
			data=line.split('	')
			if(data[0]=='USGS'):
				dt=datetime.datetime.strptime(data[2], "%Y-%m-%d").date()
				dd=data[3]
				if dd=='':
					dd='0'
				dd=float(dd)/3.28084/3.28084/3.28084
				self.reading.append(Data(dt,dd))
	
	def extract(self,y):
		r=[]
		for d in self.reading:
			if d.date.year == y:
				r.append(d)
		return r
		
	def plotAll(self):
		data=[]
		date=[]
		for d in self.reading:
			data.append(float(d.data))
			date.append(d.date.year*10000+d.date.month*100+d.date.day)
		plt.plot(date, data, 'go')
		plt.show()
	
	def plotYear(self,y):
		m=self.meanAnnual(y)
		data=[]
		date=[]
		mean=[]
		SDsum=0
		count=0
		
		for d in self.reading:
			if d.date.year==y:
				data.append(float(d.data))
				date.append(d.date.month*100+d.date.day)
				mean.append(m)
				SDsum=SDsum+(d.data-m)**2
				count=count+1
		sd=np.sqrt(SDsum/count)
		plt.plot(date, data, 'r')
		plt.plot(date, mean, 'k')
		plt.fill_between(date,mean-sd/2,mean+sd/2,facecolor='grey')
		plt.show()
		
	def meanAnnual(self,y):
		sum=0
		count=0
		for d in self.reading:
			if d.date.year == y:
				sum=sum+d.data
				count=count+1
		return sum/count
		
if __name__ == '__main__':
	h=Hydro('dv.txt')
	print h.meanAnnual(1979)
	h.plotYear(1979)
	