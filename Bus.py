class Vehicle:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def details(self):
        print(f"Name : {self.name}, Speed : {self.max_speed}, Mileage: {self.mileage}")
        
class Bus(Vehicle):
    pass

School_Bus = Bus("School Volvo", 180, 12)

print(f"Vehicle Name: {School_Bus.name}, Speed: {School_Bus.max_speed}, Mileage: {School_Bus.mileage}")

School_Bus.details()