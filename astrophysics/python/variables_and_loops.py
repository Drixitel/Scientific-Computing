import numpy as np 					#using module numpy 

def main(): 						#define function main()
	i = 0 							
	n = 10 
	x = 119.0 					 	#declaring two integers and a float 

	y = np.zeros(n,dtype= float) 	#creates an array of zeros s.t n=10 
									#n defines amount of zeros 
									#float = decimal int = integer
	
	for i in range(n): 				#n=10 so [0,9] range loop

		y[i] = 2.0 * float(i) + 1 	#indexing i begins at zero 
									# we begin at the first placement in
									# the array. preform an action and replace 
	for y_element in y: 			#after changing the values we print
		print(y_element)			# them individually 



if __name__ == '__main__': 			#if we are running from the main 
	main() 							# module run the entire module ?
