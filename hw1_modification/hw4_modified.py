#Liyan Tian
#10/20/2014
#Homework1: 
#Question4: Read data from the file drifter.dat.  Return a dictionary based on the track name as indices, returning a list of lat/lon pairs

import numpy as np

class read_drift(object):

	def __init__(self, filename):
		self.filename=filename
		f=open(self.filename)
		positions=[]
		tracks={}
		i=0
		
		for line in f.readlines():
			data=line.split('	')
			if(data[0]=='Track'):
				if i>0:
					tracks[names]=positions
				names=data[1]
				positions=[]
				i=i+1
				
			if(data[0]=='Trackpoint'):
				positions.append(((float(data[1][1:3])+float(data[1][4:10])/60.0),(float(data[1][12:14])+float(data[1][15:21])/60.0)))
		if i>0:
			tracks[names]=positions
		print tracks    #return a list of lat/lon pairs for all track names
		print tracks['FRODO']    #return a list of lat/lon paris for tracks['FRODO']

if __name__=='__main__':
	#test of read_drift function		
	filename='drifter.dat'
	tracks=read_drift(filename)    #result should return a list of lat/lon pairs for all track names, and a list of lat/lon paris for tracks['FRODO']

raw_input()
				