# Python Turtle Tutorial

In this tutorial you're going to make a game and play it programmatically.
The game is played on a 11 x 11 grid.
Your turtle can move up, down, left and right.
Your turtle must avoid rocks to get to a plant.
In the first version the game is won by reaching the plant.

## Terminology

__Python__ - python is the programming language being used. It is an interpreted language. This means it does not run natively on a computer, instead you must have Python installed and your code is interpreted by the Python program. Many languages work this way and python is the most widely used.

__Console__ - this is a little window that is running the program. Text will print in the console from the program and you can ask users for text input.

__GUI__ - the Graphical User Interface is created by your python program. The program is running in the console, and creates the GUI from there.

## Step 1: Get setup

First go to [https://replit.com/@mj1618/TurtleTutorial#README.md](https://replit.com/@mj1618/TurtleTutorial#README.md)
And click "fork" to take a personal copy of this tutorial.
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

## Step 2: ifs and for loops

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
Note that you can use `i` for your `x` or `y` coordinates.
You can also do some arithmatic in there like `i * 2` (i multiplied by 2).

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

