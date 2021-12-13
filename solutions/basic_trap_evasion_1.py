from utils.utils import pause
from utils.world import create_world

world = create_world()
world.create_rock(5, 0)
world.create_rock(5, 1)
world.create_rock(4, 1)
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
      world.move_turtle_left()
    world.move_turtle_up()

pause()
