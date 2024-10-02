class Vehicle:
    
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = float(mileage)  
        self.capacity = int(capacity)  
        
    def fare(self):
        return self.capacity * 100  
class Bus(Vehicle):
    
    def fare(self):
        amount = super().fare()
        amount = amount + amount * 10 / 100  
        return amount
    

nameVehicle = input("Enter the Name of the Vehicle: ")
mileageAmount = input("Enter the Mileage: ")
capacity = input(f"Enter the Capacity of the {nameVehicle}: ")

School_Bus = Bus(nameVehicle, mileageAmount, capacity)

print(f"Total {nameVehicle} Fare is: {School_Bus.fare()}")
