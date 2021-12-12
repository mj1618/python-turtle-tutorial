from utils.utils import pause
from utils.world import create_world

def calculate_path(world):

  if world.has_plant() == False or world.has_turtle() == False:
    print('Error, create a plant and a turtle before calculating a path')
    return None
    
  points_to = {}
  for x in range(11):
      for y in range(11):
          points_to[(x, y)] = None
  points_to[(0,0)] = (0,0)

  queue = list()
  queue.append(world.get_turtle_position())
  while len(queue) > 0 and points_to[world.get_plant_positions()[0]] == None:
    current = queue.pop(0)
    for next in world.get_positions_around(current):
      if points_to[next] == None:
        points_to[next] = current
        queue.append(next)

  if points_to[world.get_plant_positions()[0]] == None:
    return None
  else:
    path = list()
    current = world.get_plant_positions()[0]
    while current != world.get_turtle_position():
      path.append(current)
      current = points_to[current]
    
    path.reverse()
    return path


world = create_world()
world.create_plant(10, 10)
world.create_turtle(0, 0)
world.create_random_rocks(30)

path = calculate_path(world)
if path is None:
  print('There is no path for turtle to take to get to the plant! Game over...')
else:
  print('There is a path of ' + str(len(path)) + ' steps found for turtle, moving to the plant now.')
  print('The path is: ')
  print(path)
  world.move_along_path(path)

pause()
