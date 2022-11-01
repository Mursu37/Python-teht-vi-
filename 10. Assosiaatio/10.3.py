class Elevator:
    def __init__(self, min_floor, max_floor):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current = min_floor
        self.number = None

    def move_to(self, floor):
        if floor > self.current:
            count = floor - self.current
            for i in range(count):
                if self.current == self.max_floor:
                    return
                else:
                    self.move_up()

        elif self.current > floor:
            count = self.current - floor
            for i in range(count):
                if self.current == self.min_floor:
                    return
                else:
                    self.move_down()

    def move_up(self):
        self.current += 1
        print(f"Tämänhetkinen kerroksesi on {self.current}")
        return

    def move_down(self):
        self.current -= 1
        print(f"Tämänhetkinen kerroksesi on {self.current}")
        return


class House:
    def __init__(self, min_floor, max_floor, elevator_count):
        self.elevators = []
        self.min_floor = min_floor
        self.max_floor = max_floor

        for i in range(elevator_count):
            e = Elevator(self.min_floor, self.max_floor)
            e.number = i + 1
            self.elevators.append(e)

    def use_elevator(self, elevator_nr, floor):
        current_ele = self.elevators[elevator_nr-1]
        print(f"Olet hississä {current_ele.number}")
        current_ele.move_to(floor)

    def firealarm(self):
        print("Palohälyytys!")
        for elevator in self.elevators:
            elevator.move_to(elevator.min_floor)


house = House(0, 7, 3)

house.use_elevator(2, 9)
house.use_elevator(1, 5)
house.use_elevator(2, -1)
house.use_elevator(3, 3)

house.firealarm()

for elevator in house.elevators:
    print(f"Hissi {elevator.number} on kerroksessa {elevator.current}")
