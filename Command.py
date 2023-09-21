"""This code defines an abstract Command class and its concrete subclasses (MoveCommand, TurnLeft, and TurnRight). 
    Each concrete command implements an execute method that can be called on a rover object to perform the corresponding action."""
class Command:
    def execute(self, rover):
        pass

class MoveCommand(Command):
    def execute(self, rover):
        rover.move()

class TurnLeft(Command):
    def execute(self, rover):
        rover.turn_left()

class TurnRight(Command):
    def execute(self, rover):
        rover.turn_right()
