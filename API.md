# Turtle World API

  * [create_world()](#create-world--)
  * [world.create_rock(x, y)](#worldcreate-rock-x--y-)
  * [world.create_plant(x, y)](#worldcreate-plant-x--y-)
  * [world.create_turtle(x, y)](#worldcreate-turtle-x--y-)
  * [world.is\_rock_at(x, y)](#worldis--rock-at-x--y-)
  * [world.is\_rock_{direction}()](#worldis--rock--direction---)
  * [world.is_turtle_on_plant()](#worldis-turtle-on-plant--)
  * [world.move\_turtle_{direction}()](#worldmove--turtle--direction---)

## create_world()

Creates a GUI with a grid, returns a world object to do further actions from.

```py
from utils.world import create_world
world = create_world()
```

## world.create_rock(x, y)

## world.create_plant(x, y)

## world.create_turtle(x, y)

## world.is\_rock_at(x, y)

## world.is\_rock_{direction}()

- world.is_rock_right()
- world.is_rock_left()
- world.is_rock_up()
- world.is_rock_down()

Returns True if a rock is next to the turtle in the specified direction, otherwise returns False.

## world.is_turtle_on_plant()

## world.move\_turtle_{direction}()

- world.move_turtle_right()
- world.move_turtle_left()
- world.move_turtle_up()
- world.move_turtle_down()

## world.get\_rock_positions()

## world.get\_plant_positions()

## world.get\_turtle_position()


