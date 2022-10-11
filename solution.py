import random
import time

# declaring a fixed number of elevators
elevators = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: ""}
floors = None


# Function  to call  an elevator
def call_elevator(floor):
    call = 0
    if floor > floors:
        print("FLOOR NUMBER OUT OF BOUNDS!! Enter valid floor number")
    else:
        for key, value in elevators.items():
            # check if the elevator is occupied and it is the nearest available elevator
            if not elevators[key].occupied and closest_elevator(floor) == elevators[key]:
                call = key
                elevators[key].occupied = True
                elevators[key].current_floor = floor

            else:
                call = random.randint(1, 8)
    print("You have called elevator number:" + elevators[call])
    return elevators[call]


# find the closest elevator
def closest_elevator(current_floor):
    distances = []

    for key in elevators.keys():
        diff = abs(current_floor - elevators[key].current_floor)
        distances.append(diff)
        print(diff)

    least_distance = min(distances)
    print("Nearest elevator is elevator number:" + str(elevators[least_distance].elevator_num))
    return elevators[least_distance]


# define class elevator and its attributes
class Elevator:
    def __init__(self, current_floor):
        self.current_floor = current_floor
        self.floor_num = 0
        self.floors = []
        self.elevator_num = 0
        self.min_distance = 0
        self.occupied = False

    # what happens when elevator is called
    def elevator_called(self, new_floor):
        self.current_floor = new_floor
        self.occupied = True

    def min_time(self, person_floor, elevator_floor):
        self.min_distance = abs(person_floor - elevator_floor)




class Movement:
    # input current floor as a parameter
    def __init__(self, elev_num, floor=0):
        self.floor = floor
        self.elev_num = elev_num
        self.position = 0
        self.direction = None

    # string object of elevator
    def __str__(self):
        return "Elevator {} on floor {}".format(self.elev_num, self.floor)

    def __repr__(self):
        return "<Elevator object {}  on floor {}>".format(
            self.elev_num, self.floor)

    # close elevator door
    def close(self):
        print("Closing elevator {}.".format(self.elev_num))

    # open elevator door
    def open(self):
        print("Opening elevator {}.".format(self.elev_num))

    # moves elevator up and down
    def move(self, elevator):
        elevator.floors[self.floor].remove(self)
        self.position += 1
        self.floor += self.direction
        elevator.floors[self.floor].append(self)

        print("On floor {}...".format(self.floor))


floors = int(input("Enter number of floors in building:"))

# create elevators and floors
for num in range(1, 9):
    elevator = Elevator(1)
    elevator.elevator_num = num
    elevators[num] = elevator
    # time.sleep(1)
    print("creating elevator " + str(elevators[num].elevator_num), "with " + str(floors), "number of floors")

print("number of floors : " + str(floors))

print(elevators)

# instance movement


# movement = Movement(call_elevator(3), 7)

# movement.close()
# movement.open()
# movement.move(call_elevator(3))
