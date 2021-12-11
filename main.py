from utils.utils import pause
from utils.world import create_world

world = create_world()
world.create_rock(1, 1)
world.create_plant(10, 10)
world.create_turtle(0, 0)

world.move_turtle_right()
world.move_turtle_left()
world.move_turtle_up()
world.move_turtle_down()


pause()


