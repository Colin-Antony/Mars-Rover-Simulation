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