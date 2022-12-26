import numpy as np 
import sys						#imports two modules, sys is built in 


#define a function that returns a value 
#runs 3rd

def expo(x):					#define a function called expo
	return np.exp(x) 			#exp: returns an array of 1x1 value: e^x 
								#x is a parameter expo takes 

#define a subroutine that does not return a value 
#runs 2nd 

def show_expo(n): 				#n is just an input parameter 
	for i in range(n): 			#range (0,n-1) loop though it 
		print(expo(float(i)))	#calls the expo function 

		#at 0 print the value in the array 1x1: e^0 = 1 
		#at 1 print e^1 = e and so on until n-1 

#define a main function 

def main(): #runs 1st 
	n = 10 						#default value 

	#checking for command line arguments 

	if (len(sys.argv)>1): 		#if argument provided overwrite n
		n = int(sys.argv[1])	#the name of the file is index 0 llength 1
								#if more is given take the index 1 value 
	show_expo(n) 				#call the show_expo subroutine 
								#result: python functions.py 3 will 
								#print 3 values e^0, e^1, e^2 

#run the main function 

if __name__ == "__main__": 		
	main()