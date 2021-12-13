from utils.utils import pause
from utils.world import create_world

world = create_world()
world.create_rock(5, 0)
world.create_rock(5, 1)
world.create_rock(5, 2)
world.create_rock(5, 3)
world.create_rock(4, 3)
world.create_rock(3, 3)
world.create_rock(2, 3)
world.create_rock(2, 2)
world.create_rock(2, 1)
world.create_rock(3, 1)
world.create_plant(10, 10)
world.create_turtle(0, 0)

while world.is_turtle_on_plant() == False:
  if world.can_move_right():
    world.move_turtle_right()
  elif world.can_move_up():
    world.move_turtle_up()
  else:
    while world.can_move_up() == False:
      if world.can_move_left() == False:
        world.move_turtle_down()
        world.move_turtle_left()
      else:
        world.move_turtle_left()
        

      while world.can_move_down() == False:
        if world.can_move_right() == False:
          world.move_turtle_up()
          world.move_turtle_right()
        else:
          world.move_turtle_right()
      while world.can_move_down():
        world.move_turtle_down()
      while world.can_move_left():
        world.move_turtle_left()
      world.move_turtle_up()
    world.move_turtle_up()


pause()
