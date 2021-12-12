# Python Turtle Tutorial

In this tutorial you're going to make a game and play it programmatically.
The game is played on a 11 x 11 grid.
Your turtle can move up, down, left and right.
Your turtle must avoid rocks to get to a plant.
In the first version the game is won by reaching the plant.

![Turtle Screenshot](/assets/screenshot.png)

## Contents

  - [Terminology](#terminology)
  - [Step 1: Get setup](#step-1-get-setup)
  - [Step 2: Create a World](#step-2-create-a-world)
  - [Step 3: ifs and for loops](#step-3-ifs-and-for-loops)
  - [Step 4: Variables](#step-4-variables)
  - [Step 5: Lists and Maps](#step-5-lists-and-maps)
  - [Step 6: The Perfect Algorithm](#step-6-the-perfect-algorithm)
  - [Step 7: Master Level Algorithm](#step-7-master-level-algorithm)

## Terminology

__Python__ - python is the programming language being used. It is an interpreted language. This means it does not run natively on a computer, instead you must have Python installed and your code is interpreted by the Python program. Many languages work this way and python is the most widely used.

__Console__ - this is a little window that is running the program. Text will print in the console from the program and you can ask users for text input.

__GUI__ - the Graphical User Interface is created by your python program. The program is running in the console, and creates the GUI from there.

## Step 1: Get setup

First go to [https://replit.com/@mj1618/TurtleTutorial#README.md](https://replit.com/@mj1618/TurtleTutorial#README.md) and click "Fork repl" to take a personal copy of this tutorial.
You may need to create an account with repl.it if you haven't got one already.
Open the `main.py` file which you will be editing and click `Run` at the top of the page.
This should open a GUI and a console with your program running.
Adjust the size of the GUI to make it bigger if you can't see the entire grid.

## Step 2: Create a World

The only file you need to edit is `main.py`.
Other code and images sit in the folders `utils` and `assets`, you can have a look if you want but you don't need to touch these files for this tutorial.

__Imports__

```py
from utils.utils import pause
from utils.world import create_world
```

This imports some things you can use from the utils.
All it means is you can now use `pause` and `create_world` in the file.

__Create Stuff__

```py
world = create_world()
world.create_rock(1, 1)
world.create_plant(10, 10)
world.create_turtle(0, 0)
```

This creates the grid and uses the variable `world` to store things in.
You then call functions on the world to put elements on the grid.
You pass in an `x` and `y` coordinate to tell the world where to put these elements.

_Note: to see all the possible functions to call on the `world` object, see the [API Guide](./API.md)._

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

Now that you have these basics in `main.py` play around a bit.
Change the coordinates being passed in to create elements.
Repeat the movement of the turtle lines, see if you can move the turtle to the plant by doing this.
Try putting some rocks in the way of the turtle and then move the turtle around them.

Don't worry about breaking things, you can always go back to the start.
Playing and breaking things is the most important part of programming including at advanced levels.
It is a core skill you must learn and get comfortable with as it is the only way to properly test your code and to see where its limits are.
You should find some bugs in the game already by doing this.

## Step 3: ifs and for loops

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

__Challenge 1__

Use for loops to get the turtle to the plant while repeating as few lines as possible.

__Challenge 2__

Try using for loops to create rocks.
Note that you can optionally use `i` for your `x` and `y` coordinates.
You can also do some arithmatic in there like `i * 2` (i multiplied by 2).
Create a rock formation that goes across the screen from (1, 5) to (9, 5).
Can you create a diagonal line?

Extra: there are some other ways to use `range()` and you can read about them [here](https://www.w3schools.com/python/ref_func_range.asp).

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

The `%` is the modulo operator, and you can read `i % 2` as "the remained when `i` is divided by `2`.

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

Using `if/else` and `for` loops create a program that gets the turtle to the plant as best as possible.
Then test your algorithm by placing rocks in the turtles way.

Whenever you find a rock formation that your turtle can't navigate, change your turtle algorithm so it can handle all previous rock formations plus this one.

## Step 4: Variables

You may have found that it is hard for the turtle to handle all rock formations with the tools you have available so far.
One of the things you might have got stuck on is that when a turtle has a rock to the right and above, it'll need to go back.
But once it moves back it's going to try going right again, it can't remember that it already went that way.

Variables are used to remember things in programs.
Variables are set to a certain value, that value can be a number, text or many other things we'll learn about later.
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

## Step 5: Lists and Maps

## Step 6: The Perfect Algorithm

## Step 7: Master Level Algorithm

Add multiple random plants to the world.
Create an algorithm that reaches all plants (that are reachable) in the shortest possible number of moves.