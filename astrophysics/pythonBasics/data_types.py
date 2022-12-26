import numpy as np 

#integers 

i = 10 						#declare int

print(type(i))

a_i = np.zeros(i,dtype=int)	#create an array of 10 zeros, as integers
print(type(a_i))			#print the array 
print(type(a_i[0]))			#print the index 0: first value 

#floats 

x = 119.0 					#float (decimal)
print(type(x))				#print data type of x 

y = 1.19e2					#float in scientific notation 
print(type(y))				#print data type of y

z = np.zeros(i, dtype=float)#declare array of floats; amount 10
print(type(z))				#print data type of z nd array 
print(type(z[0]))			#print data type of index 0 