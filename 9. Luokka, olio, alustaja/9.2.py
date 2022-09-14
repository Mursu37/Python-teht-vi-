class Car:
    def __init__(self, reg, top_speed, current_speed=0, distance=0):
        self.reg = reg
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance = distance

    def accelerate(self, acceleration):
        if acceleration < 0:
            if self.current_speed + acceleration < 0:
                self.current_speed = 0
            else:
                self.current_speed += acceleration

        elif self.current_speed + acceleration > self.top_speed:
            self.current_speed = self.top_speed

        else:
            self.current_speed += acceleration
        return self.current_speed


car1 = Car("ABC-123", 142)

car1.accelerate(30)
print(car1.current_speed)
car1.accelerate(70)
print(car1.current_speed)
car1.accelerate(50)
print(car1.current_speed)
car1.accelerate(-200)
print(car1.current_speed)

print(f"Rekisterinumer {car1.reg}, Huippunopeus {car1.top_speed}, "
      f"Tämänhetkinen nopeus {car1.current_speed} km/h, Kuljettu matka {car1.distance}")