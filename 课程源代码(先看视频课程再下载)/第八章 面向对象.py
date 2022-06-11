from car_file import *

my_car =  Car("Audi "," A4",2013)
my_car.mod_this_year(2020)
print(my_car.this_year)
result = my_car.detection()
print(result)
my_tesla = ElectricCar("Tesla ","model s",2017)
print(my_tesla.year)
my_tesla.battery(1000)
result = my_tesla.detection()
print(result)
# print(my_tesla.year,my_tesla.this_year)
# print(my_tesla.detection())
