# a child class from the parent class Car 

class Car: 
	'''A simple attempt to represent a car.'''

	def __init__(self, make, model, year): 
		'''Initialize attributes to describe a car.'''
		# stores information as attribute 
		self.make = make 
		self.model = model 
		self.year = year 
		self.odometer_reading = 0 
		

		
	def get_descriptive_name(self):  #method 
		'''Return a neatly formatted descriptive name.'''
		long_name = f'{self.year} {self.make} {self.model}'
		return long_name.title() #not a print function

	def read_odometer(self):
		'''Print a statment showing the car's mileage.'''
		print(f'This car has {self.odometer_reading} miles on it.')


	def update_odometer(self, milage): 
		'''Set the odometer reading to the given value.
		Reject the change if it attempts to roll the 
		odometer back.'''

		if milage >= self.odometer_reading:
			self.odometer_reading = milage 
			#stored and retained for the future 
		else: 
			print("You can't roll back an odometer!")



	def increment_odometer(self, miles): 
		'''Add the given amount to the odometer
		reading.'''
		if miles >= 0: 
			self.odometer_reading += miles 
		else: 
			print('You cannot have negavite miles!')		


	def fill_gas_tank(self, fuel):
		'''Electric cars don't have gas tanks.'''
		self.fuel = fuel
		print(f"This car has {self.fuel} - gal of fuel!")


#parent class, not super(). function includedd 
class Battery: 
	'''A simple attempt to model a battery for an electric car.'''
	#note this is a set size for all E.cars 
	def __init__(self, battery_size = 75): 
		#if no value provided, will set to 75 
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



#child class 
class ElectricCar(Car): #attribute is the parent 
	'''Represent aspects of a car, specific to electric 
	vehicles.'''

	# still normal init() taking from parent
	def __init__(self, make, model, year): 
		'''Initialize attributes of the parent class.
		Then initialize attributes specific to
		an electric car.'''

		super().__init__(make, model, year)
		#super(). lets you call a method from the parent 

		
		#removed & replace below statement
		#self.battery_size = 75 #attribut of all e.cars 
		self.battery = Battery() #new call to Class (new intance)
		self.emotions_about_car = 'It is a dumb car.'

	#remove the method below and treat it as a class above
	def describe_my_feelings(self): 
		'''print a statement about my feeling about the car.'''
		#print(f'This is what I think about the car: "{self.emotions_about_car}"')

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

