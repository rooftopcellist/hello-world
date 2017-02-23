'''
Implementation of Cooley and Tukey FFT Algorithm
Author: Christian M. Adams


'''


import cmath
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image	#for later use with 2d image array

iArray = (26160.0,19011.0,18757.0,18405.0,17888.0,14720.0,14285.0,17018.0,18014.0,17119.0,16400.0,17497.0,17846.0,15700.0,17636.0,17181.0)

def FFT(d,iArray):
	# d = 1
	N = len(iArray)
	r = N//2
	#Master Loop index print
#	print("r = ", r)
	z=[]
	for i in iArray:
			z.append(i + 0j)
	print("Input: \n",z,"\n\n")
	theta = -2 * cmath.pi * d / N
	if N > 1:
			i=1
			while i <= N-1:
					k=0
					m=0
					print("i = ", i)
					w = complex(cmath.cos(i*theta), cmath.sin(i*theta))
					while k <= N-1:
							# print("k = ", k)
							u = 1
							for m in range(r):
									#This prints all of the indexes
									print("i= ", i,"k = ", k,"m = ",m, "r= ", r)
									t = z[k + m] - z[k + m + r]
									z[k + m] = z[k + m] + z[k + m +r]
									z[k+m+r] = t*u
									u = w * u
							k = k + 2*r
					r = r//2
					i = 2*i
			i=0
			for i in range(N):
					r = i
					k = 0
					m = 1
					while m <= N-1:
							k = 2*k + (r % 2)
							r = r//2
							m = 2*m
					if k > i:
							t = z[i]
							z[i] = z[k]
							z[k] = t

			if d < 0:
					i = 0
					while i <= N-1:
					##for i in range(0, N-1):
							z[i] = z[i]//N

	return z
	
	
def main():
	#Computes the FFT of the input data and stores in fftData
	fftData = FFT(1,iArray)
	print("\nResults:")
	for item in fftData:
		print(item)

		
	#Finds the complex conjugate and stores it in ccData
	print('\nComplex Conjugates:')
	ccData = []
	for item in fftData:
		temp = np.conjugate(item)
		print(temp)
		ccData.append(temp)
		
		
	#Multiplies the FFT Data and their Complex Conjugates and stores in fftccData
	print('\nProduct of Complex Conjugates and FFT Data:\n')
	fftccData = []
	i=0
	for i in range(len(fftData)):
		temp = fftData[i]*ccData[i]
		print(temp)
		fftccData.append(temp)
		print(fftccData[i].real)
		
	#Converts from Complex to Real to get Power Spectrum Density
	print('\nPSD')
	psdData = []
	i=0
	for i in range(len(fftData)):
		temp = fftccData[i].real
		print(temp)
		psdData.append(temp)

#Right now this data is Nonsensical because the input data is just random numbers TAG chose.  
#	y=psdData
	y=iArray
	plt.plot(y)
	plt.show()
	
	#Rescale data to sampling frequency
	

main()