#Liyan Tian
#10/14/2014
#Homework 2
# 4. Create a class to read discharge data for the Brazos river from this page:http://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=08116650&referred_module=sw&period=&begin_date=1967-10-01&end_date=2014-10-01
# Store date (as an array of datetime objects) and discharge data (an array of floating point
# numbers, converted to cubic meters per second) as attributes within the class.
# Create methods to:
 # - Extract a year of discharge data. Return dates and discharges for the specified year. 
 # - Plot the hydrograph over the entire length of the timeseries.

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
		
	def plot(self):
		data=[]
		date=[]
		for d in self.reading:
			data.append(float(d.data))
			date.append(d.date.year*10000+d.date.month*100+d.date.day)
		plt.plot(date, data, 'go')
		plt.show()
		
if __name__ == '__main__':
	h=Hydro('dv.txt')
	print h.extract(1968)
	h.plot()
	