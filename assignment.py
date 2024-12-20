# Activity 1: Design Your Own Class! 🏗️

class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"{self.brand} {self.model} costs ${self.price}"

    def make_call(self, number):
        return f"Calling {number} from {self.model}..."

class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, fitness_tracker):
        super().__init__(brand, model, price)
        self.fitness_tracker = fitness_tracker

    def display_info(self):
        info = super().display_info()
        return f"{info} and has a fitness tracker: {self.fitness_tracker}"

# Example usage
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 15", 1200)
    watch = Smartwatch("Apple", "Watch Series 9", 500, True)
    print(phone.display_info())
    print(phone.make_call("+123456789"))
    print(watch.display_info())

# Activity 2: Polymorphism Challenge! 🎭

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Example usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        print(vehicle.move())
