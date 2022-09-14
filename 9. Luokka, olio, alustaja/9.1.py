
class Car:
    def __init__(self, reg, top_speed, current_speed=0, distance=0):
        self.reg = reg
        self.top_speed = str(top_speed) + " km/h"
        self.current_speed = str(current_speed) + " km/h"
        self.distance = distance

car1 = Car("ABC-123", 142)

print(f"Rekisteritunnus {car1.reg}, huippunopeus {car1.top_speed}, hetkellinen nopeus "
      f"{car1.current_speed}, kuljettu matka {car1.distance}")