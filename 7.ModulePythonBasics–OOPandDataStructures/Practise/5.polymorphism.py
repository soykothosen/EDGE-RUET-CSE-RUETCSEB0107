class Boat:
    def __init__(self, speed):
        self.Speed = speed

    def Move(self):
        print("Boat is moving")

class Bike:
    def __init__(self, speed):
        self.Speed = speed

    def Move(self):
        print("Bike is moving")

class Car:
    def __init__(self, speed):
        self.Speed = speed

    def Move(self):
        print("Car is moving")

boat = Boat("4 km/hr")
bike = Bike("30 km/hr")
car = Car("60 km/hr")

boat.Move()
bike.Move()
car.Move()

print(bike.Speed)
print(boat.Speed)
print(car.Speed)