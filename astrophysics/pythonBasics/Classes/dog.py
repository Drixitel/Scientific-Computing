# each intance created from the Dog class will 
#  store a name and an age, and we'll give each
#	dog the ability to sit() and roll_over()  
#by convention classes get capital letters 
#classes do not need parenthesis 



class Dog: 
	''' A simple attempt to model a dog.'''
	def __init__(self, name, age): 
		'''Initialize name and age attributes.'''
		self.name = name
		self.age = age 

#funciton 
#this is a docstring describing what the class does
	def sit(self): 
		'''Simulate a dog sitting in response to a command.'''
		print(f"{self.name} is now sitting.")

	def roll_over(self): 
		'''Simulate rolling over in response to a command.'''
		print(f'{self.name} rolled over!')


my_dog = Dog('Willie', 6) #python will create a dog
							#it will not print anything

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

 # find an attribute value 
my_dog.name
#showing we found it 
print(my_dog.name)

my_dog.sit()
my_dog.roll_over()


your_dog = Dog('Lucy', 3)

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

