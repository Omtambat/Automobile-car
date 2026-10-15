
class Automobile:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(self.brand, "is starting")

    def display(self):
        print("Brand:", self.brand)
        print("Color:", self.color)


# Child class 1
class Car(Automobile):
    def __init__(self, brand, color, seats):
        super().__init__(brand, color)
        self.seats = seats

    def show_car(self):
        self.display()
        print("Type: Car")
        print("Seats:", self.seats)


# Child class 2
class Bike(Automobile):
    def __init__(self, brand, color, engine_cc):
        super().__init__(brand, color)
        self.engine_cc = engine_cc

    def show_bike(self):
        self.display()
        print("Type: Bike")
        print("Engine CC:", self.engine_cc)


# Create objects
car1 = Car("Toyota", "White", 5)
bike1 = Bike("Honda", "Black", 150)

print("--- Car Details ---")
car1.show_car()
car1.start()

print("\n--- Bike Details ---")
bike1.show_bike()
bike1.start()
