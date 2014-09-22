import numpy as np

def read_drift(filename):
	f=open(filename)
	
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
	return tracks	
filename='drifter.dat'
tracks=read_drift(filename)
print tracks['FRODO']

raw_input()
			