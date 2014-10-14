#Liyan Tian
#10/14/2014
#Homework 2
#Question1:Given two arrays of points (with shapes (N, 2) and (M, 2)) where the columns are x and y,
#respectively, write a function that returns an NxM matrix that defines the distance between
#each of the points in one array to each of the points in the other array.  Make sure your
#solution is vecorized (no loops!!!)

import numpy as np

N=input("please input N")
M=input("please input M")

A1=np.arange(2*N).reshape(N,2)
A2=np.arange(2*M).reshape(M,2)
O1=np.ones(N).reshape(1,N)
O2=np.ones(M).reshape(1,M)

a1x=np.dot(A1.T[0].reshape(N,1),O2)
a1y=np.dot(A1.T[1].reshape(N,1),O2)
a2x=np.dot(A2.T[0].reshape(M,1),O1).T
a2y=np.dot(A2.T[1].reshape(M,1),O1).T
dist=np.sqrt((a2x-a1x)**2+(a2y-a1y)**2)

print dist


raw_input()