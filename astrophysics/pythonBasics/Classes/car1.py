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



my_new_car = Car('audi', 'a4', 2019) #must specify

#the above is behind the scenes only print displays 
print(my_new_car.get_descriptive_name()) #call a method

my_new_car.odometer_reading = 23 # direct change 
my_new_car.read_odometer() #returns string


my_other_car = Car('honda', 'civic', 2020)


print(my_other_car.get_descriptive_name())
my_other_car.update_odometer(40)
my_other_car.read_odometer()

my_other_car.update_odometer(20)# did not work, nice 
my_other_car.read_odometer()

my_other_car.update_odometer(50)# did not work, nice 
my_other_car.read_odometer()


my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100) #logic works 
my_used_car.read_odometer()