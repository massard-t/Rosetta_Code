class door(object):
    """docstring for door"""
    def __init__(self, number):
        self.number = number
        self.state = 0

    def change_state(self):
        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 0

    def print_state(self):
        print(self.state)

doors = []
for x in range(1, 101):
    doors.append(door(x))
    pass

print(len(doors))

for x in range(1, 101):
    for door in doors:
        if door.number % x is not (not 0):
            door.change_state()

for door in doors:
    door.print_state()
