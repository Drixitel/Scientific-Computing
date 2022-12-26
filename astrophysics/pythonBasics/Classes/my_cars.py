from car import Car, ElectricCar

my_beetle = Car('vw', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster',2019)
print(my_tesla.get_descriptive_name())


import car 

my_beetle = car.Car('vw', 'reddy', 2020)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'booomby', 2020)
print(my_tesla.get_descriptive_name())