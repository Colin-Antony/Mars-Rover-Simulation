Hello EI Team. I have chosen the first problem statment: Simulating a Mars Rover that can navigate a grid based terrain.

# Mars-Rover-Simulation
A robust and efficient grid based Mars Rover simulation that demonstrates OOP prinicples, SOLID principles, Exception Handling abilty and Validations.

### The code is well documented. For any detailed explaination just open the codes. 'How code works' below should cover a rough idea.
### Thought process is explained in 'Thought Process.docx' along with all OOPS and SOLID principles present in my project.  
  
To Run the final version of the code. Run 'Final Command Interface.py'. This includes full functionality of the project along with excellent exception handling. Follow along the instructuions that appear on console when the code is run.  
To Run a mini version that only shows how MarsRover class and Command is implemented, run the 'PrefixedCommands.py' file.  

## How code works  
1) Class RoverStart is a child class of GridObstacle which is in turn a child class of GridManager.
2) GridManager has instance variables, getters and setters, and validation methods that are used in the child classes.  
3) GridObstacle handles Grid Creation and Obstacle Placing. GridException is a subclass of the python Exception class that handles any custom exceptions to do with error in user inputs that arent syntactically wrong.
4) RoverStart handles the starting positon of the rover. RoverException works same as GridException but for RoverStart.  
5) MarsRover handles the movement logic of the rover. Detects obstacles and skips the command if it leads to a crash. Also has a status report method that outputs where the rover finally ends up.
6) Commands class is an abstract class with 3 child classes: MoveForward, TurnLeft and TurnRight. This is where polymorphism is expertly demonstrated in the code.
7) InterfaceCommands is a set of methods that are called in Final Command Interface.py to make the code more readable and easy to debug. It is responsible for accepting user inputs and putting into play the Exception Handling messages mentioned earlier.  


## Exception Handling  
Here is a list of the custom exceptions handled by my code using the Exception classes created  
  
1) Grid dimensions are validated: Integer/float only. Only 2d coordinate accepted  
2) Obstacle placing: Obstacle should be within the grid.  
3) Rover Placing: Rover cannot be placed on an obstacle and should be within the grid. Direction the rover faces(Orientation) should also be a valid one. All conditions must satisfy.
4) Movement Commands: Movement commands are validated. Only M, L and R is accepted.  
5) Coordinate inputs: Anytime coordinates are accepted from the user, we make sure it is a non empty list or tuple. We also ensure if the values within it are int or float only.  

When any of the above exceptions occur along with some unmentioned trivial ones. The user is asked to re-enter the values. Note that for obstacle detection if any one coordinate is invalid, all coordinates must be re-entered.  
   

## General Notes about the code  
Used time.sleep() methods to make the console outputs more readable by delaying the output.  

## Output Screenshots
![image](https://github.com/Colin-Antony/Mars-Rover-Simulation/assets/123204978/ce198a12-dc45-4bc9-8d81-26799372f870)  
![image](https://github.com/Colin-Antony/Mars-Rover-Simulation/assets/123204978/b4363e68-484a-4152-b342-1ca662ba617c)  
![image](https://github.com/Colin-Antony/Mars-Rover-Simulation/assets/123204978/c08432ad-341e-49cb-bd43-60409a48eca3)  

Open 'Exception Handling Screenhots' to see some types of exception handling and input validation the code performs"  


## HAPPY EXPLORING
