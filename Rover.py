from Grid_and_obstacle import *
import time


# Handles custom exceptions raised by rover start
class RoverException(Exception):
    pass


"""This class handles the starting position of the rover. It ensures that the rover is not placed on any obstacle
    It is a child class of GridObstacle and inherits all its methods and instance variables"""


class RoverStart(GridObstacle):
    #class variables that are later used to retrieve the start values
    startx=None
    starty=None

    def start_position(self, start): # Validates the start input coordinate (x,y,direction(N,E,W,S))

        listcheck, message = self.check_list(start) # Validates if input is a list or tuple and not null.
        if not listcheck:
            raise RoverException(message)
        valid, message1 = self.valid_start(start, self.x, self.y) # Validates the x y and direction values
        if valid:
            print(f"{start} is a valid coordinate.")
            self._matrix[start[0]][start[1]] = "R" # R represents start position of rover
            self._orientation = start[2]
            self.startx = start[0]
            self.starty = start[1]
        else:
            raise RoverException(message1) # Raises exception message obtained from valid_start if input is invalid

    def valid_start(self, Start_Coordinates, x, y):
        directions = {"N", "E", "W", "S"} # To later check if input is valid
        if not isinstance(Start_Coordinates, (list, tuple)) or len(Start_Coordinates) != 3: # Raise exception if length and datatype is invalid
            return False, f"{Start_Coordinates} is not a valid start coordinate.\nEnsure you have input the x, y and direction in the mentioned format"
        if not (isinstance(Start_Coordinates[0], (int, float)) and isinstance(Start_Coordinates[1], (int, float))): # Raise exception if first 2 values in input list
            return False, f"{Start_Coordinates} is invalid. First 2 elements can only be tuple or array"
        if Start_Coordinates[0] > x - 1 or Start_Coordinates[1] > y - 1: # Raises Exception if 1st 2 values are outside the range
            return False, f"{Start_Coordinates} is out of range. Place objects within({x - 1},{y - 1}).\n (Remember " \
                          f"the grid is 0 indexed.) "
        if Start_Coordinates[2] not in directions: # Raises Exception if direction is invalid
            return False, f"{Start_Coordinates} is invalid. Coordinates are valid but direction is invalid"
        if self._matrix[Start_Coordinates[0]][Start_Coordinates[1]] == "x": # Rais
            return False, f"ALERT. There is an obstacle "
        return True, f"{Start_Coordinates} is valid" # If code reaches here, start coordinates were valid


# if __name__ == "__main__":
#     Grid = create_grid()
#     place_objects(Grid)
#     start_rover(Grid)
#     print("Your Grid: ")
#     mat = Grid.get_matrix()
#     for row in mat:
#         print(row)
#     time.sleep(1)
#     print(f"Your rover is facing {Grid.get_orientation_word()}")
