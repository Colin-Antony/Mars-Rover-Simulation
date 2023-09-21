import time


# class that contains size of the grid
class Grid:

    def __init__(self, x, y):
        self.x = x - 1
        self.y = y - 1


# class that has all the rover operational logic
class MarsRover():

    def __init__(self, grid, start_x, start_y, direction, obstacles):

        self.grid = grid  # Object with grid dimensions x and y
        # start coordinates
        self.x = start_x
        self.y = start_y

        self.direction = direction  # direction orientation of rover
        self.obstacles = obstacles  # set of obstacles

    def is_obstacle(self, x, y): # checks if a coordinate is an obstacle
        return (x, y) in self.obstacles

    """Verifies the forward move by checking if the position it is moving to is not an obstacle and within bounds
        If not. Mentions to the user that there is an obstacle"""
    def move(self):
        if self.direction == "N" and self.x > 0:
            if not self.is_obstacle(self.x - 1, self.y):
                self.x -= 1
            else:
                self.obstacle_alert(self.x - 1, self.y)
        elif self.direction == "S" and self.x + 1 < self.grid.x:
            if not self.is_obstacle(self.x + 1, self.y):
                self.x += 1
            else:
                self.obstacle_alert(self.x + 1, self.y)
        elif self.direction == "E" and self.y + 1 < self.grid.y:
            if not self.is_obstacle(self.x, self.y + 1):
                self.y += 1
            else:
                self.obstacle_alert(self.x, self.y + 1)
        elif self.direction == "W" and self.y > 0:
            if not self.is_obstacle(self.x, self.y - 1):
                self.y -= 1
            else:
                self.obstacle_alert(self.x, self.y - 1)

    def obstacle_alert(self, a, b):
        print(f"ALERT: Obstacle at ({a}, {b}). SKIPPING COMMAND")
        time.sleep(1)

    # Below to functions change the orientation of the rover. Self explanatory
    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"

    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"

    # Executes the commands passed in by the user. Refer to command.py for more clarity
    def execute_commands(self, commands):
        for command in commands:
            command.execute(self)

    # Status report
    def get_status_report(self):
        dirs = {"N": "North", "S": "South", "E": "East", "W": "West"}
        return f"Rover is at {self.x},{self.y} facing the {dirs[self.direction]}."
