#string

s = 'I am a string.'
print(type(s))					#sting

#Boolean 

yes = True
print(type(yes))				#Boolean True

no = False 
print(type(no))					#Boolean False 

#List -- ordered and changable 

alpha_list = ['a','b', 'c']		#declared list 
print(type(alpha_list))			#touple? what why? 
print(type(alpha_list[0]))		#string, index 0 : 'a'
alpha_list.append('d')			#add 'd' to end of list
print(alpha_list)				#print list 


#Tuple -- ordered and unchangeable 

alpha_tuple = ('a','b','c')		#declared tuple 
print(type(alpha_tuple))		#pring data type 

try: 							#lets you test a block
	alpha_tuple[2] = 'd' 		#this should give an error 
except TypeError: 				#lets you handle the error
	print("We can't add elements to tuples!")
print(alpha_tuple)				#prints tuple 