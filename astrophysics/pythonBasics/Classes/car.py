''' A class that can be used to represent a car. '''
# the above is a module level docstring 
# it is to describe the module car 

class Car: 
	'''A simple attempt to represent a car.'''

	def __init__(self, make, model, year):
		'''Initialize attributes to describe a car.'''
		#what it takes in 
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0 

	def get_descriptive_name(self): 
		'''Return a neatly descriptive name.'''
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

		#run this method and return a string 
		#takes no inputs 

	def read_odometer(self):
		'''print a statement showing the car's mileage.'''
		print(f'This car has {self.odometer_reading} miles on it.')

		#run this method and print a string 
		#takes no inputs 


	def update_odometer(self, mileage):
		'''
		Set the odometer reading to the given value.
		Reject the change if it attempt to roll back. 
		'''
		if mileage >= self.odometer_reading: 
			self.odometer_reading = mileage
		else: 
			print("You can't roll back an odometer!")


		#run this method, take an imput and increment 
		#if input is larger then saved value deny 

	def increment_odometer(self, miles):
		'''Add the given amount to the odometer reading.'''
		self.odometer_reading += miles 


class Battery: 
	'''A simple attempt to model a battery for an electric car.'''
	
	def __init__(self, battery_size = 75): 
		
		'''Initialize the battery's attributes.'''
		self.battery_size = battery_size

	def describe_battery(self):
		'''Print a statement describing the battery size.'''

		print(f"This car has a {self.battery_size} - kWh battery.")
		
	def get_range(self): 
		'''Print a statement about the range this battery provides.'''
		if self.battery_size == 75: 
			range = 260
		elif self.battery_size == 100: 
			range = 315
		print(f"This car can go about {range} miles on a full charge.")




class ElectricCar(Car): #attribute is the parent 
	'''Represent aspects of a car, specific to electric 
	vehicles.'''


	def __init__(self, make, model, year): 
		'''Initialize attributes of the parent class.
		Then initialize attributes specific to
		an electric car.'''

		super().__init__(make, model, year)
	
		self.battery = Battery() 
		self.emotions_about_car = 'It is a dumb car.'

	
	def describe_my_feelings(self): 
		'''print a statement about my feeling about the car.'''
		print(f'This is what I think about the car: "{self.emotions_about_car}"')

	def fill_gas_tank(self):
		'''Electric cars don't have gas tanks.'''
		print("This car doesn't need a gas tank!")




class Battery: 
	'''A simple attempt to model a battery for an electric car.'''
	
	def __init__(self, battery_size = 75): 
		'''Initialize the battery's attributes.'''
		
		self.battery_size = battery_size

	def describe_battery(self):
		'''Print a statement describing the battery size.'''

		print(f"This car has a {self.battery_size} - kWh battery.")
		
	def get_range(self): 
		'''Print a statement about the range this battery provides.'''
		if self.battery_size == 75: 
			range = 260
		elif self.battery_size == 100: 
			range = 315
		print(f"This car can go about {range} miles on a full charge.")
