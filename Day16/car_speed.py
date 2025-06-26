class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
            self.speed -= 5
       
    def display_speed(self):
        print(f"The current speed of {self.brand} {self.model} is {self.speed} km/h.")


car = Car("Toyota", "Corolla")

print(f"Car: {car.brand} {car.model}")
car.display_speed()

car.accelerate()
car.display_speed()

car.accelerate()
car.display_speed()

car.brake()
car.display_speed()

car.brake()
car.display_speed()



