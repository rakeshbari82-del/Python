# 🚗 FUTURE VEHICLE BUILDER 🚀

class Vehicle:
    def __init__(self, brand, speed, color):
        self.brand = brand
        self.speed = speed
        self.color = color

    def show_details(self):
        print("Brand       :", self.brand)
        print("Top Speed   :", self.speed, "km/h")
        print("Color       :", self.color)

    def move(self):
        print("🚘 The vehicle is moving...")


# 🚗 Child Class 1
class ElectricCar(Vehicle):
    def __init__(self, brand, speed, color, battery):
        super().__init__(brand, speed, color)
        self.battery = battery

    def show_details(self):
        print("\n⚡ ELECTRIC CAR")
        super().show_details()
        print("Battery     :", self.battery, "%")

    def move(self):
        print("⚡ The electric car moves silently!")


# 🏍️ Child Class 2
class SuperBike(Vehicle):
    def __init__(self, brand, speed, color, engine_cc):
        super().__init__(brand, speed, color)
        self.engine_cc = engine_cc

    def show_details(self):
        print("\n🏍️ SUPER BIKE")
        super().show_details()
        print("Engine      :", self.engine_cc, "cc")

    def move(self):
        print("🔥 The super bike races at high speed!")


# 🚁 Child Class 3
class FlyingCar(Vehicle):
    def __init__(self, brand, speed, color, flight_range):
        super().__init__(brand, speed, color)
        self.flight_range = flight_range

    def show_details(self):
        print("\n🚁 FLYING CAR")
        super().show_details()
        print("Flight Range:", self.flight_range, "km")

    def move(self):
        print("🚀 The flying car takes off into the sky!")



# Creating Objects

car = ElectricCar("Tesla", 250, "Red", 95)
bike = SuperBike("Kawasaki", 300, "Green", 1000)
flying_car = FlyingCar("SkyDrive", 500, "White", 300)


# Display Details

car.show_details()
car.move()

bike.show_details()
bike.move()

flying_car.show_details()
flying_car.move()


# Checking Inheritance

print("\n🔍 INHERITANCE CHECK")

print(
    "Is ElectricCar a subclass of Vehicle?",
    issubclass(ElectricCar, Vehicle)
)

print(
    "Is SuperBike a subclass of Vehicle?",
    issubclass(SuperBike, Vehicle)
)

print(
    "Is FlyingCar a subclass of Vehicle?",
    issubclass(FlyingCar, Vehicle)
)