import random


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

    def move(self, hours):
        self.distance = self.distance + self.current_speed * hours


competing_cars = []
for count in range(10):
    car = Car("ABC-" + str(count), random.randint(100, 200))
    competing_cars.append(car)

race_not_over = True
while race_not_over:
    for cars in competing_cars:
        cars.accelerate(random.randint(-10, 15))
        cars.move(1)
        if cars.distance >= 10000:
            race_not_over = False


for cars in competing_cars:
    print(f"{cars.reg}, {cars.top_speed}, {cars.current_speed}, {cars.distance}")
