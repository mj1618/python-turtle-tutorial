import turtle
from .config import NUM_GRID_ROWS, RIGHT, LEFT, UP, DOWN, CELL_WIDTH
from .utils import position_to_coord

class MyTurtle():
  current_direction = RIGHT
  turtle_object = None
  x = None
  y = None
  in_motion = False
  world = None

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.turtle_object = turtle.Turtle()
    self.turtle_object.hideturtle()
    self.turtle_object.color('#402e08')
    self.turtle_object.shape('turtle')
    self.turtle_object.penup()
    self.turtle_object.setposition(position_to_coord(self.x, self.y))
    self.turtle_object.showturtle()

  
  def move_up(self):
    
    if self.in_motion is True:
      print('Ignoring movement as turtle is already moving')
      return
    if self.y == NUM_GRID_ROWS - 1:
      print('Can\'t move turtle up, there is a wall there')
      return
      

    self.in_motion = True
    if self.current_direction == RIGHT:
      self.turtle_object.left(90)
    elif self.current_direction == UP:
      pass
    elif self.current_direction == DOWN:
      self.turtle_object.left(180)
    elif self.current_direction == LEFT:
      self.turtle_object.right(90)
    self.current_direction = UP
    self.turtle_object.forward(CELL_WIDTH)
    self.y += 1
    self.in_motion = False


  def move_down(self):
    

    if self.in_motion is True:
      print('Ignoring movement as turtle is already moving')
      return
    if self.y == 0:
      print('Can\'t move turtle down, there is a wall there')
      return
      
    if self.in_motion is True:
      return
    self.in_motion = True
    if self.current_direction == RIGHT:
      self.turtle_object.right(90)
    elif self.current_direction == UP:
      self.turtle_object.right(180)
    elif self.current_direction == DOWN:
      pass
    elif self.current_direction == LEFT:
      self.turtle_object.left(90)
    self.current_direction = DOWN
    self.turtle_object.forward(CELL_WIDTH)
    self.y -= 1
    self.in_motion = False


  def move_left(self):
    
    if self.in_motion is True:
      print('Ignoring movement as turtle is already moving')
      return
    if self.x == 0:
      print('Can\'t move turtle left, there is a wall there')
      return
      
    if self.in_motion is True:
      return
    self.in_motion = True
    if self.current_direction == RIGHT:
      self.turtle_object.left(180)
    elif self.current_direction == UP:
      self.turtle_object.left(90)
    elif self.current_direction == DOWN:
      self.turtle_object.right(90)
    elif self.current_direction == LEFT:
      pass
    self.current_direction = LEFT
    self.turtle_object.forward(CELL_WIDTH)
    self.x -= 1
    self.in_motion = False
    
  def move_right(self):
    
    if self.in_motion is True:
      print('Ignoring movement as turtle is already moving')
      return
    if self.x == NUM_GRID_ROWS - 1:
      print('Can\'t move turtle right, there is a wall there')
      return
      
    if self.in_motion is True:
      return
    self.in_motion = True
    if self.current_direction == RIGHT:
      pass
    elif self.current_direction == UP:
      self.turtle_object.right(90)
    elif self.current_direction == DOWN:
      self.turtle_object.left(90)
    elif self.current_direction == LEFT:
      self.turtle_object.right(180)
    self.current_direction = RIGHT
    self.turtle_object.forward(CELL_WIDTH)
    self.x += 1
    self.in_motion = False


  def position(self):
    return (self.x, self.y)

