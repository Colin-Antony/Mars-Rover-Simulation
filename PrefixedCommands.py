from Command import *
from RoverMove import *


"""This code is a set of commands that are already entered just to get a small feel of the code and to debug any issues in
    MarsRover and Command classes. Do execute if you would like to. But main code is in Final Command Interface.py"""

grid = Grid(10,10)
obstacles={(2,2),(3,5)}
rover = MarsRover(grid, 3,3, 'E', obstacles)
commands = [MoveCommand(),MoveCommand(),MoveCommand(),MoveCommand(),TurnLeft(),MoveCommand(),TurnRight(),MoveCommand()]
rover.execute_commands(commands)
print(rover.get_status_report())