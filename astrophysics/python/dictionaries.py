#define a dictionary data structure 

#dictionaries have key: value for the elements 

example_dict = {
	'class'			:	'Astr 119',
	'prof'			: 	'Brant', 
	'awesomeness'	: 	10 
}
print(type(example_dict)) 			#gives data type 

#get a value via key 

course = example_dict['class'] 	 	#assign a variable call values with []
print(course)						#print 'Astr 119'

#change a value via key
example_dict['awesomeness'] += 1 	#increment by 1 
									#since the key is a int
									#symbols for int work 

#print the dictionary 
print(example_dict)

#print dictionary element by element 
for x in example_dict.keys():			#only interested in keys
	print(x,example_dict[x])		#loop through them 
									#also print values x is paired with