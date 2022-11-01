import random


class Car:
    def __init__(self, reg, top_speed, distance=0):
        self.reg = reg
        self.top_speed = top_speed
        self.current_speed = 0
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


class Competition:
    def __init__(self, name, goal, competing_cars=None):
        self.name = name
        self.goal = goal
        self.competing_cars = competing_cars
        self.time = 0

    def create_cars(self, count):
        if self.competing_cars is None:
            self.competing_cars = []
        for i in range(count):
            car = Car("ABC-" + str(i+1), random.randint(100, 200))
            self.competing_cars.append(car)

    def hour_pass(self):
        for cars in self.competing_cars:
            cars.accelerate(random.randint(-10, 15))
            cars.move(1)
        self.time += 1

    def print_stats(self):
        print(f"Aikaa on mennyt {self.time} tuntia")
        for cars in self.competing_cars:
            print(f"{cars.reg}, {cars.top_speed}, {cars.current_speed}, {cars.distance}")

    def competition_over(self):
        for cars in self.competing_cars:
            if cars.distance >= self.goal:
                self.print_stats()
                print(f"{cars.reg} Voitti")
                return True


race = Competition("Suuri romuralli", 8000)
race.create_cars(10)

race_running = True
while race_running:
    race.hour_pass()
    if race.competition_over():
        race_running = False
        break

    if race.time % 10 == 0:
        race.print_stats()
