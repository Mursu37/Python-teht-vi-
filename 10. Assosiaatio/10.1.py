class Elevator:

    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.current = min

    def move_to(self, floor):
        if floor > self.current:
            count = floor - self.current
            for i in range(count):
                if self.current == self.max:
                    return
                else:
                    self.move_up()

        elif self.current > floor:
            count = self.current - floor
            for i in range(count):
                if self.current == self.min:
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

h = Elevator(-1, 12)

h.move_to(0)
h.move_to(-3)
h.move_to(10)
h.move_to(2)
h.move_to(13)
