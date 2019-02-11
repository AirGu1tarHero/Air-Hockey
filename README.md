# Air-Hockey

This is a representation of an Air Hockey game programmed in Python.
The code utilizes a module called the Arcade library, which is a Python library
based on the popular Pygame module. A 2D physics model is provided by the
Pymunk module, which is a Python port of the Chipmunk physics engine.

The main function is run from the game.py file, with a graphics and physics file
providing functionality. There are two game states, "Paused" and "Action".
The board is drawn with the Arcade library whilst the puck and strikers are
loaded as sprites.

Player controls the right-hand striker with the mouse and serves the puck by
clicking the mouse button. The game continues until the player quits via
the Ctrl-Q or Cmd-Q keys.

This game is submitted as my final project for the Harvard-X CS50 course.
Please enjoy!
