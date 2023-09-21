from Rover import *
from Grid_and_obstacle import *
from RoverMove import *
from Command import *

"""Objective of these functions are to make the interface codes neater. Basically functions that preprocess the input
    from the user and checks for any exceptions and raises appropriate messages"""


# Calling Grid creation after validating user inputs. Retries if user input is invalid
def create_grid():
    print("Enter dimensions -> x,y")
    while True:
        try:
            n = input().split(",")  # Splits input into an array when it finds a comma
            if len(n)>2:
                print("Enter only x and y coordinate")
                continue
            n = [int(x.strip()) for x in n]  # Removes any dummy whitespaces
            Rover = RoverStart(n[0], n[1])
            # Exception raising
        except Creation_Exception as c:
            print(f"Error: {c}.\nRetry")
        except Exception as e:
            print(f"Error: {e}.\nRetry")
        else:
            print(f"Grid initialized with dimensions{Rover.get_size()}")
            return Rover


#
def place_objects(Rover):
    print("Enter number of obstacles")
    # verifying input as integer
    while True:
        try:
            n = int(input())
        except ValueError:
            print(f"INVALID. Enter a number")
        else:
            break
    if n == 0:
        print("Not placing obstacles")
        return

    print("Enter obstacles one by one. Separate x and y values with a comma")
    # Calling Obstacke placing after validating user inputs. Retries if user input is invalid
    while True:
        try:
            lst = []
            for _ in range(n):
                lst.append(list(map(int, input().split(","))))  # appending all user inputs to lst
            Rover.place_obstacles(lst) # Places obstacles. Raises custom exception if present.
        except RoverException as r:
            print(f"Error: {r}")
            print(f"Obstacles not placed")
        except GridException as g:
            print(f"Error: {g}")
            print(f"Obstacles not placed")
        except Exception as e:
            print(f"Invalid Input. {e}")
            print(f"Obstacles not placed")
        else:
            time.sleep(1)
            print("Obstacles placed succesfully")
            time.sleep(1)
            break


def start_rover(Rover):
    print("Enter start coordinates in the form: x,y,N or S or E or W.\n"
          "Enter within the range of the grid you created and don't place it on top of obstacles.")
    while True:
        lst = input().split(",") # splits user input into a list after every comma
        try:
            lst = [x.strip() for x in lst] # Removes leading and trailing whitespaces
            lst[0] = int(lst[0])
            lst[1] = int(lst[1])
            Rover.start_position(lst) # Checks if start position is valid. Raises custom exceptions as well
        except RoverException as r:
            print(f"Error: {r}.\nRetry")
        except Exception as e:
            print(f"Error: {e}.\nRetry")
        else:
            print("Placing rover")
            time.sleep(1) # To make code easy to read
            print("Rover placed Successfully")
            time.sleep(1)
            break


def enter_commands():
    val_commands = {"M", "L", "R"}
    while (True):
        n = input("Enter a line of commands (M,L and R). Let them be space separated.\n").split()
        flag = True
        for command in n:
            if command.strip() not in val_commands: # strip removes trailing and leading whitespaces
                flag = False # flag set to false if command is invalid
        if flag:
            break
        else:
            print("Invalid commandset. Re-Enter.")

    print("Commands are valid... Executing")
    time.sleep(1)
    return n

# converts the user input commands to their respective classes. Refer command.py for clarity
def execute(commands):
    dict = {"M": MoveCommand, "L": TurnLeft, "R": TurnRight}
    comms = []
    for command in commands:
        comms.append(dict[command]())
    return comms
