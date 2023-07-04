from car import Car
from random import choice, randint

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def read_odometer(self):
        #!
        """Overriding method in the class Car."""
        print(f"This electic car has {self.odometer_reading} miles on it.")    

if __name__ == "__main__":
    my_tesla = ElectricCar('tesla', 'model s', 2019)
    my_beetle = Car('volkswagen', 'beetle', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()
    #! using python standard lib, and the random module
    car_list = [my_tesla, my_beetle]
    """
    randint takes two integer arguments and returns a randomly selected integer
    between (and including) those numbers
    choice selects an item from a list or tuple randomly 
    """
    print("I need you to buy", randint(1,3), "of", f'"{choice(car_list).get_descriptive_name()}"s')