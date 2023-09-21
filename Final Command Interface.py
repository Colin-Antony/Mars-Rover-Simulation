import time
from InterfaceCommands import *
from RoverMove import *
from Command import *


"""This code calls all the helper functions we created to make the code neater. It accepts user inputs runs them through
    all the exception handling, validates the inputs, passes them on down to the MarsRover class after validation. Inputs are 
    thoroughly validated and all custom exceptions so far have been handled. ENJOY YOUR TIME WITH THE ROVER. Code is very self explanatory
    as most of it involves calling Interface Commands."""

Visual_Grid = create_grid() # Initializes grid
place_objects(Visual_Grid)
start_rover(Visual_Grid)
print("Your Grid: ")
mat = Visual_Grid.get_matrix()
for row in mat:
    print(row)

time.sleep(1)
print(f"Your rover is facing {Visual_Grid.get_orientation_word()}")
comms = enter_commands() # Checks validity of commands and returns them
x , y = Visual_Grid.get_size()
grid = Grid(x,y)
rover = MarsRover(grid, Visual_Grid.startx, Visual_Grid.starty, Visual_Grid.get_orientation(), Visual_Grid.obstacles) # initializes MarsRover
formatted = execute(comms) # Converts the commands from L,R,M to the actual classes. Refer Commands.py for clarity
rover.execute_commands(formatted)
print(rover.get_status_report())
time.sleep(1)
mat[rover.x][rover.y] = "Re" # Represents end location of rover
print("Final grid position is:")
for row in mat:
    print(row)
print("Rover started at R and ended at Re. If you dont't see an R that means rover started and ended in the same place")
print("Rover moved successfully avoiding the obstacles and staying within the grid!!")