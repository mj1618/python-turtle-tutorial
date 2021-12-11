import turtle
from .config import PLANT, ROCK, GRID
import sys
from .turtle import MyTurtle
from .rock import Rock
from .plant import Plant

my_world = None

def close():
  sys.exit()

class World():
  screen = None
  my_turtle = None
  rocks = []
  plants = []
  def __init__(self):
    self.screen = turtle.getscreen()
    turtle.hideturtle()
    
    self.screen.addshape(PLANT)
    self.screen.addshape(ROCK)
    self.screen.bgpic(GRID)
    self.screen.bgcolor('black')
    self.screen.setup(800, 600,startx = 0,
            starty = 0)

    # self.screen.setworldcoordinates(0, 0, 520, 520)
    canvas = self.screen.getcanvas()
    canvas.itemconfig(self.screen._bgpic)

    self.screen.onkeypress(close, "Escape")

    turtle.onkey(self.move_turtle_up, 'Up')
    turtle.onkey(self.move_turtle_down, 'Down')
    turtle.onkey(self.move_turtle_left, 'Left')
    turtle.onkey(self.move_turtle_right, 'Right')
    turtle.listen()

  def create_turtle(self, x, y):
    if self.my_turtle is None:
      self.my_turtle = MyTurtle(x, y)
    return self.my_turtle
  
  def create_rock(self, x, y):
    rock = Rock(x, y)
    self.rocks.append(rock)

  def create_plant(self, x, y):
    plant = Plant(x, y)
    self.plants.append(plant)

  def is_rock_right(self):
    for rock in self.rocks:
      if rock.x - 1 == self.my_turtle.x and rock.y == self.my_turtle.y:
        return True
    return False

  def is_rock_left(self):
    for rock in self.rocks:
      if rock.x + 1 == self.my_turtle.x and rock.y == self.my_turtle.y:
        return True
    return False
  def is_rock_up(self):
    for rock in self.rocks:
      if rock.x == self.my_turtle.x and rock.y - 1 == self.my_turtle.y:
        return True
    return False
  def is_rock_down(self):
    for rock in self.rocks:
      if rock.x == self.my_turtle.x and rock.y + 1 == self.my_turtle.y:
        return True
    return False

  def is_turtle_on_plant(self):
    for plant in self.plants:
      if plant.x == self.my_turtle.x and plant.y == self.my_turtle.y:
        return True
    return False

  def move_turtle_down(self):
    if self.is_rock_down():
      print('Can\'t move turtle down, there is a rock there')
      return
    self.my_turtle.move_down()
    self.check_on_plant()

  def move_turtle_up(self):
    if self.is_rock_up():
      print('Can\'t move turtle up, there is a rock there')
      return
    self.my_turtle.move_up()
    self.check_on_plant()

  def move_turtle_right(self):
    if self.is_rock_right():
      print('Can\'t move turtle right, there is a rock there')
      return
    self.my_turtle.move_right()
    self.check_on_plant()

  def move_turtle_left(self):
    if self.is_rock_left():
      print('Can\'t move turtle left, there is a rock there')
      return
    self.my_turtle.move_left()
    self.check_on_plant()
  
  def check_on_plant(self):
    if self.is_turtle_on_plant():
      print('Turtle is on top of a plant, good job!')

  def turtle_position(self):
    return self.my_turtle.position()

  def is_rock_at(self, x, y):
    for rock in self.rocks:
      if rock.x + 1 == self.my_turtle.x and rock.y == self.my_turtle.y:
        return True
    return False
  
def create_world():
  global my_world
  if my_world is None:
    my_world = World()
  return my_world
