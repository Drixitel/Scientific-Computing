#python exceptions let you deal with 
#unexpected results 

try: 
	print(a)
except: 
	print('a is not defined!')	#a is not defined, this will print

#there are specific errors to help with cases 
try: 
	print(a)
except NameError: 
	print('a is still not defined!') #also true, and will print

except: 
	print('Something else went wrong.')


#This will break our program 
#since a is not defined 
print(a)