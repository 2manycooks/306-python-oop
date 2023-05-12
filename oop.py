# class CoffeeCup():

#     def __init__(self, capacity, amount = 0):
#         self.capacity = capacity
#         self.amount = amount

#     def __str__(self):
#         if(self.amount == 0):
#             return "iz empty"
#         else:
#             return f"iz not empty, haz {self.amount}oz left"

#     def fill(self):
#         self.amount = self.capacity

#     def drink(self, drink_amount):
#         self.amount -= drink_amount
#         if(self.amount <= 0):
#             self.amount = 0

#     def empty(self):
#         self.amount = 0



# # gabes_cup = CoffeeCup(8)
# # westons_cup = CoffeeCup(16)
# # abdallahs_cup = CoffeeCup(32)
# # new_cup = CoffeeCup(20, 10)

# # print(new_cup)

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0

#     def __str__(self):
#         return f"We've got here a {self.year} {self.make} {self.model} for sale! Don't worry, it's moving at {self.speed}mph!"
    
#     def accelerate(self, amount):
#         self.speed += amount
#         print(f"broom broom, we're going {self.speed}mph")
        
#     def brake(self, amount):
#         self.speed -= amount
#         print(f"skrrt skrrt, we're going {self.speed}mph")


# gabes_new_car = Car("Volvo", "Cross Country", 2023)
# juans_car = Car("Subaru", "Ascent", 2020)

# print(juans_car)
# juans_car.accelerate(100)
# juans_car.brake(20)


# <------------ INHERITANCE ------------>

class Phone:
    def __init__(self, phone_number):
        self.number = phone_number

    def __str__(self):
        return f"ringa ding ding, it's {self.number}"
    
    def call(self, other_number):
        print(f"Why are you calling me, {self.number}? It's 2023. Hang up and text me at {other_number}")
    
    def text(self, other_number, msg):
        print(f"texting {other_number} from {self.number}")
        print(msg)

gabes_phone = Phone("666-6666")

class IPhone(Phone):
    def __init__(self, phone_number, generation, color, fingerprint = None):
        super().__init__(phone_number)
        self.generation = generation
        self.color = color
        self.fingerprint = fingerprint

    def __str__(self):
        return f"ooh look at me i've got an iphone{self.generation} and its {self.color} ooooooh 💰"
    
    def set_fingerprint(self, new_fingerprint):
        self.fingerprint = new_fingerprint
        print(f"you have set your fingerprint to {self.fingerprint}")

    def unlock(self, fingerprint):
        if (not self.fingerprint):
            print("You didn't set up fingerprints so your phone is unlocked.")
        elif (fingerprint == self.fingerprint):
            print("Fingerprint recognized. Phone unlocked.")
        else:
            print("Fingerprint NOT recognized 🚨 Phone locked!")


# gabes_iphone = IPhone("777-7777", 14, "Rose Gold")

# gabes_iphone.set_fingerprint("Gabe")

# gabes_iphone.unlock("Gabe")

class Android(Phone):

    def __init__(self, phone_number, keyboard):
        super().__init__(phone_number)
        self.keyboard = keyboard

    def __str__(self):
        return f"Your current keyboard is set to {self.keyboard}"
    
    def set_keyboard(self, new_keyboard):
        self.keyboard = new_keyboard


gabes_android = Android("9999999", "US")
print(gabes_android)
gabes_android.set_keyboard("UK")
print(gabes_android)