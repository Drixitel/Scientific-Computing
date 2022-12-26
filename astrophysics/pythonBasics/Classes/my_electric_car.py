from car import ElectricCar as ECar

my_tesla = ECar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() #preset value
my_tesla.battery.get_range() #preset value 