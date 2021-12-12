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

Create a rock at (x, y)

## world.create_plant(x, y)

Create a plant at (x, y)

## world.create_turtle(x, y)

Create a turtle at (x, y)

## world.is\_rock_at(x, y)

Returns `True` if a rock is currently at (x, y), returns False otherwise.

## world.is\_rock_{direction}()

- world.is_rock_right()
- world.is_rock_left()
- world.is_rock_up()
- world.is_rock_down()

Returns True if a rock is next to the turtle in the specified direction, otherwise returns False.

## world.is_turtle_on_plant()

Returns True if the turtle is on top of the plant and the game is won.

## world.move\_turtle_{direction}()

- world.move_turtle_right()
- world.move_turtle_left()
- world.move_turtle_up()
- world.move_turtle_down()

Move the turtle one step in the specified direction.
Will not move the turtle into walls or into rocks.
Prints a winning message to the screen if the turtle moves onto a plant.

## world.get\_rock_positions()

Returns a `list` of tuples of all the positions of the rocks currently on the grid.

E.g.
```py
[(1, 1), (1, 2), (1,3)]
```

## world.get\_plant_positions()

Returns a `list` of tuples of all the positions of the plants currently on the grid.
The tutorial only ever uses one plant.

## world.get\_turtle_position()

Returns a tuple of the turtle's position.

## world.create_random_rocks(number_of_rocks)

Create the specified number of rocks in random positions.

## world.get_positions_around(position)

Return a list of the up, down, left, right coordinates around the given argument `position`.
Only includes points that are within the grid and do not have rocks.

## world.take_step(position)

Move the turtle one step to the specified `position`.
If the position is not right next to the turtle this function does nothing.

## world.move_along_path(path)

Move step by step along the given path.
`path` is a list of positions in-order and the turtle should be able to move from one to the next.

## world.has_plant()

Returns `True` if a plant has been added to the world, `False` otherwise.

## world.has_turtle()

Returns `True` if a turtle has been added to the world, `False` otherwise.
