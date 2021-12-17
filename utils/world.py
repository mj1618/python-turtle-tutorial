import turtle
from .config import PLANT, ROCK, GRID, NUM_GRID_ROWS
import sys
from .turtle import MyTurtle
from .rock import Rock
from .plant import Plant
import random
import time

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

  def get_rock_positions(self):
    return [(rock.x, rock.y) for rock in self.rocks]
  
  def get_plant_positions(self):
    return [(plant.x, plant.y) for plant in self.plants]

  def get_turtle_position(self):
    return (self.my_turtle.x, self.my_turtle.y)

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

  def can_move_right(self):
    return self.is_rock_right() is False and self.my_turtle.x < NUM_GRID_ROWS - 1

  def can_move_left(self):
    return self.is_rock_left() is False and self.my_turtle.x > 0

  def can_move_up(self):
    return self.is_rock_up() is False and self.my_turtle.y < NUM_GRID_ROWS - 1

  def can_move_down(self):
    return self.is_rock_down() is False and self.my_turtle.y > 0

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
      if rock.x == x and rock.y == y:
        return True
    return False

  
  def create_random_rocks(self, number_of_rocks):
    turtle.tracer(False)

    remaining_positions = set()
    for x in range(11):
      for y in range(11):
          remaining_positions.add((x, y))

    if self.has_turtle() is True:
      remaining_positions.remove(self.get_turtle_position())  # turtle starting point
    if self.has_plant() is True:
      remaining_positions.remove(self.get_plant_positions()[0])  # plant finish point

    for i in range(number_of_rocks):
      (x, y) = random.choice(tuple(remaining_positions))
      self.create_rock(x, y)
      remaining_positions.remove((x, y))
    turtle.tracer(True)
    turtle.update()
    

  def get_positions_around(self, position):
    ls = list()
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dir in dirs:
      new_pos = (position[0] + dir[0], position[1] + dir[1])
      if new_pos[0] >= 0 and new_pos[0] < 11 and new_pos[1] >= 0 and new_pos[1] < 11 and self.is_rock_at(new_pos[0], new_pos[1]) == False:
        ls.append(new_pos)
    return ls

  def take_step(self, step):
    current = self.get_turtle_position()
    if step[0] == current[0] - 1:
      self.move_turtle_left()
    elif step[0] == current[0] + 1:
      self.move_turtle_right()
    elif step[1] == current[1] - 1:
      self.move_turtle_down()
    elif step[1] == current[1] + 1:
      self.move_turtle_up()

  def move_along_path(self, path):
    for step in path:
      self.take_step(step)

  def has_plant(self):
    return len(self.plants) > 0

  def has_turtle(self):
    return self.my_turtle is not None
  
def create_world():
  global my_world
  if my_world is None:
    my_world = World()
  return my_world
