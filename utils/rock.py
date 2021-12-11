import turtle
from .config import ROCK
from .utils import position_to_coord

class Rock():
  turtle_object = None
  x = None
  y = None
  
  def __init__(self, x, y):
    self.turtle_object = turtle.Turtle()
    self.turtle_object.hideturtle()
    self.turtle_object.shape(ROCK)
    self.turtle_object.penup()
    self.turtle_object.goto(position_to_coord(x,y))
    self.turtle_object.showturtle()
    self.x = x
    self.y = y

  def position(self):
    return (self.x, self.y)

