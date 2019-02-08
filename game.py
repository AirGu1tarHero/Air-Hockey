"""
*************************        AIR HOCKEY         ****************************

                             Christopher Dobson
                              15 February 2019
                             CS50 FINAL PROJECT

*******************************************************************************

This source code leverages the Python Arcade library (http://arcade.academy):
Copyright (c) 2018 Paul Vincent Craven

The Arcade library is licensed under the MIT License.

Permission has been granted to use the Arcade library software according to the
permission notice located at: http://arcade.academy
"""
import arcade
from graphics import *

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "AIR HOCKEY"


class Game(arcade.Window):
    # Main application class

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        # Create sprite lists here and set them to None

    def setup(self):
        # Create any sprites and sprite lists here
        pass

    def on_draw(self):
        # Render the screen
        # Clear the screen to the background color, and erase the last frame.
        arcade.start_render()

        # Draw board
        draw_board()

        # Call draw() on any sprite lists here

    def update(self, delta_time):
        """
        All movement and game logic goes here.
        Call update() on any sprite lists that need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        # Called whenever a key on the keyboard is pressed
        pass

    def on_key_release(self, key, key_modifiers):
        # Called when user releases a previously pressed key
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        # Called whenver the mouse moves
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        # Called when the user presses a mouse button
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        # Called when the user releases a mouse button
        pass



def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
