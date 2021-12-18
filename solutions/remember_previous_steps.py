from utils.utils import pause
from utils.world import create_world

world = create_world()
world.create_random_rocks(30)
world.create_plant(10, 10)
world.create_turtle(0, 0)

dict = {}

for x in range(11):
  for y in range(11):
    dict[(x,y)] = list()

while world.is_turtle_on_plant() == False:
  if 'RIGHT' not in dict[world.get_turtle_position()] and world.can_move_right():
    dict[world.get_turtle_position()].append('RIGHT')
    world.move_turtle_right()
  elif 'UP' not in dict[world.get_turtle_position()] and world.can_move_up():
    dict[world.get_turtle_position()].append('UP')
    world.move_turtle_up()
  elif 'LEFT' not in dict[world.get_turtle_position()] and world.can_move_left():
    dict[world.get_turtle_position()].append('LEFT')
    world.move_turtle_left()
  elif 'DOWN' not in dict[world.get_turtle_position()] and world.can_move_down():
    dict[world.get_turtle_position()].append('DOWN')
    world.move_turtle_down()
      

pause()
