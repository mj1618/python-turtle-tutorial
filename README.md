# Python Turtle Tutorial

In this tutorial you're going to make a game and play it programmatically.
The game is played on an 11 x 11 grid.
Your turtle can move up, down, left and right.
Your turtle must avoid rocks to get to a plant.
The game is won by reaching the plant.

![Turtle Screenshot](/assets/screenshot.png)

## Contents

  - [Terminology](#terminology)
  - [Step 1: Get setup](#step-1-get-setup)
  - [Step 2: Create a World](#step-2-create-a-world)
  - [Step 3: for loops, while loops and if/else](#step-3-for-loops-while-loops-and-ifelse)
  - [Step 4: Variables](#step-4-variables)
  - [Step 5: Lists and Dictionaries](#step-5-lists-and-dictionaries)
  - [Step 6: Shortest Path Algorithm](#step-6-shortest-path-algorithm)
  - [Step 7: Master Level Algorithm](#step-7-master-level-algorithm)

## Terminology

__Python__ - python is the programming language being used. It is an interpreted language. This means it does not run natively on a computer, instead you must have Python installed and your code is interpreted by the Python program. Many languages work this way and python is the most widely used.

__Console__ - this is a little window that is running the program. Text will print in the console from the program and you can ask users for text input.

__GUI__ - the Graphical User Interface displays images/graphics and is created by your python program. The program is running in the console, and creates the GUI from there.

__Tuple__ - pronounced "too-pull", is a python value with two parts to it and created with round brackets, e.g. `x = (1, 2)`. These are used to represent x/y coordinates in the turtle game.

__Data Structure__ - a list, dictionary or any other construct for storing data in a convenient and efficient way

__Algorithm__ - a sequence of steps that achieves an outcome. Often algorithms require a certain understanding to the crux of a problem to become clear.

__Function__ - a block of code that can be called by a name and round brackets. E.g. `the_function()`.

__Object__ - objects are a more complicated construct that you don't need to understand fully for this tutorial. Objects store data, but also have functions. The only object we will be referring to is the `world` object.

__Comment__ - this is used to add notes to code, but are ignored by the program itself. Comments start with a `#` character and continue to the end of the line.

## Step 1: Get setup

First go to [https://replit.com/@mj1618/TurtleTutorial](https://replit.com/@mj1618/TurtleTutorial) and click "Fork repl" to take a personal copy of this tutorial.
You may need to create an account with repl.it if you haven't got one already.
Open the `main.py` file which you will be editing and click `Run` at the top of the page.
This should open a GUI and a console with your program running.
Adjust the size of the GUI to make it bigger if you can't see the entire grid.
You can click on the GUI to focus it, and then use arrow keys to move the turtle around.

## Step 2: Create a World

The only file you need to edit is `main.py`.
There is a `main_original.py` which is a copy of main you can use if you need to go back to the original program.
Other code and images sit in the folders `utils` and `assets`, you can have a look if you want but you don't need to touch these files for this tutorial.
The `solutions` folder contains some nifty solutions to the game which you can look at if you are stuck for ideas later on in the tutorial.

__Imports__

```py
from utils.utils import pause
from utils.world import create_world
```

This imports some things you can use from the utils.
All it means is you can now use the functions `pause` and `create_world` in the file.

__Create Stuff__

```py
world = create_world() # create the world object
world.create_rock(1, 1) # call a function on world to create a rock
world.create_plant(10, 10) # a plant
world.create_turtle(0, 0) # and your turtle
```

This creates the grid and uses the variable `world` to store the object in.
You then call functions on the world to put elements on the grid.
You pass in an `x` and `y` coordinate to tell the world where to put these elements.

_Note: to see all the possible functions to call on the `world` object, see the [API Guide](./docs/API.md)._

__Move the Turtle__

```py
world.move_turtle_right()
world.move_turtle_left()
world.move_turtle_up()
world.move_turtle_down()
```

These are the functions you call to move the turtle in each direction.
It won't allow you to hit a rock or the walls and will print a message to the console when you try to.

__Pause__

```py
pause()
```

This pauses the program so that it doesn't exit until you tell it to.
Try removing it and you will see the program starts, everything happens as expected, but then it exits and closes down immediately.
It's not important, just keep it at the end so the program stays running.

__Have a play__

Now that you have these basics in `main.py`, play around a bit.
Change the coordinates being passed in to create elements.
Repeat the movement of the turtle lines, see if you can move the turtle to the plant by doing this.
Try putting some rocks in the way of the turtle and then move the turtle around them.

Don't worry about breaking things, you can always go back to the start.
Even at advanced levels playing and breaking things is a core part of programming.
It is a  skill you must learn and get comfortable with as it is the only way to properly test your code and to see where its limits are.
You should find some bugs in the game already by doing this.

## Step 3: for loops, while loops and if/else

One way to get the Turtle to the plant is to repeat the line `world.move_turtle_right()` 10 times, and then repeat the line `world.move_turtle_up()` 10 times.
You should see something printed to the console congratulating you for reaching the plant.

This isn't very efficient.
Imagine if the grid was 1000 x 1000.
Now you've got a very repetitive program.

__for loops__

There's a programmatic way to do something repetitively with a lot less code:
```py
for i in range(10):
  print(i)
```

This will print 10 numbers to the console.
The `range()` function always starts with `0` as the first number, so the numbers printed will be `0` through to `9` inclusive.

The tab space in front of `print` is quite important, it is making it clear this line is part of the for loop.
You can add many lines inside the for loop and the block of code will repeat.
To add a line outside the for loop, simply don't add a tab space at the beginning of the line.

```py
for i in range(10):
  print(i)
print('this will only print once')
```

_Note: python takes spaces very seriously, one space forward or back and python will think this is a different block of code._

__Challenge 1__

Use for loops to get the turtle to the plant while repeating as few lines as possible.

__Challenge 2__

Try using for loops to create rocks.
Note that you can optionally use `i` for your `x` and `y` coordinates.
You can also do some arithmatic in there like `i * 2` (i multiplied by 2).
Create a rock formation that goes across the screen from (1, 5) to (9, 5).
Can you create a diagonal line?

Extra: there are some other ways to use `range()` and you can read about them at [https://www.w3schools.com/python/ref_func_range.asp](https://www.w3schools.com/python/ref_func_range.asp).

__While Loops__

While loops are similar to for loops, except instead of moving through a list of numbers it continues until some condition is met.
It can accomplish the same thing as a for loop, but can also be used in other circumstances.

```py
a = 0
while a < 10:
  a = a + 1
```
This accomplishes the same as our first for loop.

```py
while world.is_turtle_on_plant() == False:
  world.move_turtle_right()
```
Here's an example that's not like a for loop.
We want to keep repeating a block of code until the turtle reaches the plant.

__if statements__

What if we only want to do something if a particular condition is true.
For example: we only want to move up if there's no rock there.

This is what "if"s are used for.

Let's say we only want to print even numbers in our above for loop.
Here's how to do that with an if:

```py
for i in range(10):
  if i % 2 == 0:
    print(i)
```

The `%` is the modulo operator, and you can read `i % 2` as "the remainder when `i` is divided by `2`.

You'll notice only even numbers are printed to the console.
Now try printing just odd numbers, or just numbers divisible by 3.
Once again: play and try to break it.

Notice that we also add yet another tab in front of the `print`.
This indicates the `print` is now part of the `if` statement, and the `if` is part of the `for` loop.

__else statements__

`if` has a counterpart called `else`.
It allows you to do one thing on a certain condition, otherwise (or else) do something else.
Let's say we want to print a number if it's even, otherwise print the number plus ten.

```py
for i in range(10):
  if i % 2 == 0:
    print(i)
  else:
    print(i + 10)
```

__ifs With Your Turtle__

Use the `world.is_rock_{direction}()` functions to determine if there is a rock next to your turtle.
Use this function inside an if/else to help the turtle navigate around rocks, something like:

```py
if world.is_rock_right() == True:
  world.move_turtle_up()
else:
  world.move_turtle_right()
```

__Challenge__

Using `if/else` and `for` loops create a program that gets the turtle to the plant.
Then test your algorithm by placing rocks in the turtles way.

Whenever you find a rock formation that your turtle can't navigate, change your turtle algorithm so it can handle all previous rock formations plus this one.

## Step 4: Variables

You may have found that it is hard for the turtle to handle all rock formations with the tools you have available so far.
One of the things you might have got stuck on is that when a turtle has a rock to the right and above, it'll need to go back.
But once it moves back it's going to try going right again, it can't remember that it already went that way.

Variables are used to remember things in programs.
Variables are set to a certain value.
That value can be a number, text or many other things.
For now we'll stick to numbers and text.

```py
a = 1
print(a)
a = a * 2 + 1
print(a)
```

What will print to the screen is a `1` followed by a `3`.

__Challenge__

Calculate the sum of the numbers from 1 to 100 using a `for` loop and a variable.

__Text Variables__

Variables can also hold text, which in programming are called "strings".
You can concatenate strings using the plus symbol.

```py
a = "Hello, there."
a = a + " My name is J".
print(a)
```

This will print "Hello, there. My name is J" to the console.

You can use variables to hold the last direction the turtle went in.

```py
last_direction = "LEFT"

if world.is_rock_up() == True:
  if last_direction == "LEFT":
    world.move_turtle_left()

if world.is_rock_up() == False:
  if last_direction == "LEFT":
    world.move_turtle_up()
```

This will help you get past the issue described previously of remembering the turtle's last direction and navigating tricky rock formations.

__Challenge__

Use variables, if/else and for loops to get past tricky rock formations.
Tricky rock formations may include:
- a line from (1, 1) to (10, 1)
- a line from (1, 1) to (1, 10)
- a diagonal from (2, 1) to (10, 9)
- a diagonal from (10, 0) to (1, 9)
- a line from (10, 5) to (5, 5) and another line from (5, 5) to (5, 1). This is a three sided square (including the wall) designed to trap the turtle (though it has one way to get out).
- same as previously, but placed wherever the turtles natural path goes so you are forced to navigate through the three-sided square

## Step 5: Lists and Dictionaries

Variables are great and all, however they're a bit limiting.
Imagine we don't have just one number, but a list of numbers with a particular order e.g. if we wanted to remember all the moves our turtle has made thus far.
Python provides `list()` to allow us to do that.

As for Dictionaries (or what other languages call maps), imagine we wanted to look variables up based on their key.
For example: if we had multiple turtles, and wanted to look up each turtles position based on the turtles name.

__Lists__

Let's dive into some code for lists.

```py
x = list() # our variable is now a list of elements, not just a single element.
x.append(1)
x.append(2)
print(x)
```

This program will print `[1, 2]` to the console.

`x.pop()` can then be used to remove an element from the back of a list and return it's value.

```py
x = list()
x.append(1)
x.append(2)
value = x.pop()
print(value)
print(x)
```

This will print `2` followed by `[1]`.
You don't actually have to remove an element in a list to get it, you can also get it by knowing its index.
Indexes start at 0 for the first element and go on from there.

```py
x = list()
x.append(1)
x.append(2)
print(x[1])
```
Will print `2` to the console.

You can also pop an element from any index, here's how to pop from the front:
```py
x = list()
x.append(1)
x.append(2)
value = x.pop(0)
print(value)
```
Will print `1` this time.

As always: have a play, try to break it!

__Dictionaries__

Dictionaries can be described a bit simpler than lists, the only operation you really need to know to use dictionaries is how to set a `key` to a `value`.
Think of keys like names for variables.

```py
x = {} # creates a new dictionary on x
x['a'] = 1
x['b'] = 2
print(x['a']) # prints 1
print(x) # prints {a: 1, b: 2}
```

Have a play, break it, and read up more if you need more information here: [https://www.programiz.com/python-programming/dictionary](https://www.programiz.com/python-programming/dictionary)

## Step 6: Shortest Path Algorithm

For this challenge you will need the following tools mastered:
- if/else and for loops
- lists and dictionaries
- `world` functions:
  - [world.create_rock()](./docs/API.md#worldcreate_rockx-y)
  - [world.create_turtle()](./docs/API.md#worldcreate_turtlex-y)
  - [world.create_plant()](./docs/API.md#worldcreate_plantx-y)
  - [world.get_turtle_position()](./docs/API.md#worldget_turtle_position)
  - [world.get_plant_positions()](./docs/API.md#worldget_plant_positions)
  - [world.get_positions_around()](./docs/API.md#worldget_positions_aroundposition)
  - [world.create_random_rocks()](./docs/API.md#worldcreate_random_rocksnumber_of_rocks)
  - [world.move_along_path()](./docs/API.md#worldmove_along_pathpath)
- and an understanding of the [Shortest Path Algorithm](https://medium.com/algorithms-digest/shortest-path-in-a-grid-with-obstacles-elimination-ad0c07ed41c2)

The sequence of steps for the algorithm is as follows:
- create a dictionary `points_to` whose keys are coordinate tuples and values are coordinate tuples. Think of `points_to` as the grid, but with each position pointing to an adjacent position.
- set `points_to[turtle_starting_point]` to itself. This is used by the algorithm to know when to stop.
- set all other `points_to` coordinates on the grid to `None`. This indicates we haven't searched those positions yet.
- create a list called `queue` that has one element: the turtles starting position. Think of this as the list of positions we are going to search next.
- iterate while the `queue` still has values to search, and `points_to[plant_position]` is None
  - `pop` from the front of the queue into `current`
  - get positions around current using `world.get_positions_around(current)`
  - for loop over these positions using the `next` variable
    - set `points_to` for `next` to `current` (i.e. indicating `next` points to `current`)
    - append `next` to `queue`
- if `points_to[plant_position]` is `None` it means there is no valid path
- else follow the chain of `points_to` from the plant position back to the turtle
- use the list of positions (the `path`) generated to pass into `world.move_along_path(path)`. _Note it will need to be ordered from the turtle starting position as the first position._

This is a tough challenge and involves an algorithm and some data structures.
Even seasoned developers may not have come across this type of problem and may struggle, so don't worry if you don't get it straight away.

Data Structures are frequently used in day-to-day software development roles and this is a great exercise to learn some.
Algorithms are a branch of Computer Science that is rarely used in day-to-day software development, but it is worth at least learning the Shortest Path Algorithm to get an appreciation for these elusive beasts.

The solution is available here if you get stuck: [./solutions/shortest_path.py](./solutions/shortest_path.py).

## Step 7: Master Level Algorithm

Add multiple random plants to the world.
Create an algorithm that reaches all plants (that are reachable) in the shortest possible number of moves.

You will need the above shortest path algorithm, plus some of your own flare to figure out how to hit all plants.
Start with what's called a "brute-force" algorithm: come up with every possible order of plants and solve for every order, then select the one that results in the least number of turtle steps.

If you accomplish that, try to do it in a more efficient way than brute-force.
