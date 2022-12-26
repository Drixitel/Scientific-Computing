x = [0.0, 3.0, 5.0, 2.5, 3.7]	#defined array 
print(type(x))					#gives type 

#remove the 3rd element 
x.pop(2)						#index [2] is position 3
print(x)						#print overwritten x array 

#remove the element equal to 2.5 
x.remove(2.5)					#removes all instances of 2.5
print(x)						#prints new list 

#add an element to the end 
x.append(1.2)					#append adds to the end 
print(x)						#prints new list 

#get a copy 
y = x.copy()					#assign the copy to a value
print(y)						#print to show copy 

#how many elements are 0.0
print(y.count(0.0))				#gives count in y 
	
#print the index with value 3.7 
print(y.index(3.7))				#gives index value in y 

#sort the list 
y.sort()						#permanent action 
print(y)

#reverse sort 
y.reverse()						#permanent action 
print(y)

#remove all elements 
y.clear()
print(y)