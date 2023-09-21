from GridManager import *


# Handles all custom exceptions made in GridObstacle class


class GridException(Exception):
    pass


"""GridObstacle handles grid creation and obstacle placing exceptions and visualizations. It is a child class of
    GridManager and it inherits all methods and instance variables"""


class GridObstacle(GridManager):

    def __init__(self, x, y):
        super().__init__(x, y)
        # checks if x and y are valid integers and if they are greater than 1 which ensures a proper grid
        if not (isinstance(self.x, (int, float)) and isinstance(self.y, (int, float))):
            raise Creation_Exception(f"Not Valid Integer")
        if self.x < 2 or self.y < 2:
            raise Creation_Exception(f"Grid too small. Increase dimensions")
        self.obstacles = set() # set that contains the coordinates of the obstacles

    def place_obstacles(self, obstacles):
        valid, message = self.verify_obstacles(obstacles) # verifies if the list of obstacles is valid (within range of grid and if input is list or tuple)
        print(message)
        if valid:
            print("Placing obstacles")
            for obstacle in obstacles:
                self._matrix[obstacle[0]][obstacle[1]] = "x"
                self.obstacles.add((obstacle[0], obstacle[1])) # adding obstacle to the set
        else:
            raise GridException(f"Obstacles not placed.{message}") # Exception message raised when list of obstacles is invalid

    def get_obstacles(self):
        return self.obstacles

    def verify_obstacles(self, obstacles):

        valid, message = self.check_list(
            obstacles)  # checks if obstacles is a valid list or tuple, also checks if it is empty
        # valid is a boolean. Message is a string
        if valid:
            # iterates through the coordinates
            for obstacle in obstacles:
                valid1, message1 = self.valid_coordinate(obstacle, self.x, self.y)  # checks if obstacle is a valid coordinate
                if not valid1:
                    raise GridException(message1)
            return True, "Obstacles are valid"
        else:
            return valid, message


# if __name__ == "__main__":
#     commands = []
#     Rover_Grid = GridObstacle(5, 5)
#     try:
#         Rover_Grid.place_obstacles([[4, 4], [3, 3], [2, 1], [1, 2]])
#     except GridException as e:
#         print(f"Error: {e}")
#         print(f"Obstacles not placed")
#     except Exception as e:
#         print(f"Error: {e}")
#     else:
#         print("Obstacles placed")
#
#     mat = GridManager.get_matrix()
#     for row in mat:
#         print(row)
