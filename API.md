# Turtle World API

  - [create_world()](#create_world)
  - [world.create_rock(x, y)](#worldcreate_rockx-y)
  - [world.create_plant(x, y)](#worldcreate_plantx-y)
  - [world.create_turtle(x, y)](#worldcreate_turtlex-y)
  - [world.is\_rock_at(x, y)](#worldis_rock_atx-y)
  - [world.is\_rock_{direction}()](#worldis_rock_direction)
  - [world.is_turtle_on_plant()](#worldis_turtle_on_plant)
  - [world.move\_turtle_{direction}()](#worldmove_turtle_direction)
  - [world.get\_rock_positions()](#worldget_rock_positions)
  - [world.get\_plant_positions()](#worldget_plant_positions)
  - [world.get\_turtle_position()](#worldget_turtle_position)
  - [world.create_random_rocks(number_of_rocks)](#worldcreate_random_rocksnumber_of_rocks)
  - [world.get_positions_around(position)](#worldget_positions_aroundposition)
  - [world.take_step(position)](#worldtake_stepposition)
  - [world.move_along_path(path)](#worldmove_along_pathpath)
  - [world.has_plant()](#worldhas_plant)
  - [world.has_turtle()](#worldhas_turtle)
  
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

## world.create_random_rocks(number_of_rocks)

## world.get_positions_around(position)

## world.take_step(position)

## world.move_along_path(path)

## world.has_plant()

## world.has_turtle()
