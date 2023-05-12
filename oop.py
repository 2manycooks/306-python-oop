class CoffeeCup():

    def __init__(self, capacity, amount = 0):
        self.capacity = capacity
        self.amount = amount

    def __str__(self):
        if(self.amount == 0):
            return "iz empty"
        else:
            return f"iz not empty, haz {self.amount}oz left"

    def fill(self):
        self.amount = self.capacity

    def drink(self, drink_amount):
        self.amount -= drink_amount
        if(self.amount <= 0):
            self.amount = 0

    def empty(self):
        self.amount = 0



# gabes_cup = CoffeeCup(8)
# westons_cup = CoffeeCup(16)
# abdallahs_cup = CoffeeCup(32)
# new_cup = CoffeeCup(20, 10)

# print(new_cup)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def __str__(self):
        return f"We've got here a {self.year} {self.make} {self.model} for sale! Don't worry, it's moving at {self.speed}mph!"
    
    def accelerate(self, amount):
        self.speed += amount
        print(f"broom broom, we're going {self.speed}mph")
        
    def brake(self, amount):
        self.speed -= amount
        print(f"skrrt skrrt, we're going {self.speed}mph")


gabes_new_car = Car("Volvo", "Cross Country", 2023)
juans_car = Car("Subaru", "Ascent", 2020)

print(juans_car)
juans_car.accelerate(100)
juans_car.brake(20)