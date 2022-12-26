#define a function 

def flow_contorl(k): 		#arb. name 

	#define a string based on the value of k 
	if k == 0: 
		s = 'Variable k = %d equals 0.' %  k  #if value k = 0, s gets %k =k
	elif k == 1: 
		s = 'Variable k = %d equals 1.' % k 
	else: 
		s = 'Variable k = %d does not equal 0 or 1.' % k 

	print(s) 				#result of comparison 

#define a main function 

def main(): 

	#declare an integer

	i = 0 

	flow_contorl(i)

	i = 1  					#overwrite i, use flow_control to compare 

	flow_contorl(i)

	i = 2 					#overwrite i, use flow_control to compare

	flow_contorl(i) 

#run the program 
if __name__ == "__main__": 
	main()