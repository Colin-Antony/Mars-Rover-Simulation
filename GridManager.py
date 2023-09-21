# class of methods that check validity
class Creation_Exception(Exception):
    pass


""" Manages the creation, visualization and has some functions that will be used by the child classes.
    Has Getter and Setters. Has 2 validation methods(validate_coordinate and check_list) that are used by the child classes"""


class GridManager():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._matrix = [[0 for _ in range(y)] for _ in range(x)]
        self._orientation = "N"

    def get_size(self):
        return self.x, self.y # returns grid size

    def set_rover_pos(self, x, y, orientation): # setter method(for debugging purposes)
        self.x = x
        self.y = y
        self._orientation = orientation

    def get_orientation(self):
        return self._orientation

    def get_orientation_word(self): # converts letter to actual direction.
        dirs = {"N": "North", "S": "South", "E": "East", "W": "West"}
        return dirs[self.get_orientation()]

    def get_matrix(self):
        return self._matrix

    def valid_coordinate(self, coordinate, x, y): # Validates a of coordinates that is input by the user
        if not isinstance(coordinate, (list, tuple)) or len(coordinate) != 2: # checks if coordinate size is a list and of length 2
            return False, f"{coordinate} is not a valid coordinate."

        if not (isinstance(coordinate[0], (int, float)) and isinstance(coordinate[1], (int, float))): # checks if both values are integers
            return False, f"{coordinate} is invalid. Only float and int are accepted"

        if coordinate[0] > x - 1 or coordinate[1] > y - 1: # checks if coordinate is within the range of the grid
            return False, f"{coordinate} is out of range. Place objects within({x - 1},{y - 1}).\n (Remember " \
                          f"the grid is 0 indexed.) "

        return True, "Coordinate is valid"

    def check_list(self, lst):
        # checks if it is a list
        if not isinstance(lst, (list, tuple)):
            return False, "Input is not a list"

        # checks if the list is not empty
        if not lst:
            return False, "Input is empty"

        return True, "Input is a list"
