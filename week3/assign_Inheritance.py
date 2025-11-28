class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def start_engine(self):
        return f"{self.brand} Car start with key."

class Mortorcycle(Vehicle):
    def __init__(self, brand, has_sidecar):
        super().__init__(brand)
        self.has_sidecar = has_sidecar

    def start_engine(self):
        return f"{self.brand} Motorcycle start with button."
    
if __name__ == "__main__":
    car = Car("Toyota", 4)
    motorcycle = Mortorcycle("Harley-Davidson", False)

    print(car.start_engine())
    print(motorcycle.start_engine())

V = Vehicle("Generic")
C = Car("Toyota", 5)
M = Mortorcycle("Honda", has_sidecar=True)

print(f'Vehicle Brand: {V.brand}')
print(f'Car Brand: {C.brand}, Doors: {C.doors}')
print(f'Motorcycle Brand: {M.brand}, Has Sidecar: {M.has_sidecar}')