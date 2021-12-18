from utils.utils import pause
from utils.world import create_world

world = create_world()
world.create_rock(1, 1)
world.create_plant(10, 10)
world.create_turtle(0, 0)

ls = list()

ls.append(world.get_turtle_position())

world.move_turtle_right()
ls.append(world.get_turtle_position())
world.move_turtle_right()
ls.append(world.get_turtle_position())

ls.reverse()

world.move_along_path(ls)

pause()
