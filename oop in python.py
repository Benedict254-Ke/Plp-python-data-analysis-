# Assignment 1: Design Your Own Class 🏗️

# Base class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery  # in percentage
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")
    
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged. Battery: {self.battery}% 🔋")


# Inherited class
class SmartPhonePro(Smartphone):
    def __init__(self, brand, model, battery, camera_megapixels):
        super().__init__(brand, model, battery)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"{self.brand} {self.model} takes a photo with {self.camera_megapixels}MP camera 📸")


# Assignment 2: Polymorphism Challenge 🎭

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("Car is Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Plane is Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Boat is Sailing 🚤")


# Main program
if __name__ == "__main__":
    # Assignment 1 test
    phone1 = Smartphone("Samsung", "Galaxy A15", 50)
    phone1.call("123-456-789")
    phone1.charge(30)

    pro_phone = SmartPhonePro("Apple", "iPhone 15 Pro", 80, 48)
    pro_phone.call("987-654-321")
    pro_phone.take_photo()
    pro_phone.charge(10)

    print("\n--- Polymorphism Challenge ---")

    # Assignment 2 test
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        v.move()  # Each one behaves differently