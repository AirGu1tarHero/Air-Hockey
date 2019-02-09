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
# from physics import *

class Game(arcade.Window):
    # Main application class

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set mouse pointer to disappear inside the window (white background)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WHITE)

        # Create the puck
        self.puck = Puck()

        # Create the strikers
        self.npc_striker = Striker(SCREEN_WIDTH / 10, SCREEN_HEIGHT / 2,\
                                   STRIKER_RADIUS)
        self.player_striker = Striker(SCREEN_WIDTH - (SCREEN_WIDTH / 10),\
                                      SCREEN_HEIGHT / 2, STRIKER_RADIUS)

    def setup(self):
        # Create any sprites and sprite lists here
        self.puck.drop_puck()

    def on_draw(self):
        # Render the screen
        # Clear the screen to the background color, and erase the last frame.
        arcade.start_render()

        # Draw board
        draw_board()

        # Call draw() on puck and strikers
        self.puck.draw()
        self.npc_striker.draw()
        self.player_striker.draw()

    def update(self, delta_time):
        # All movement and game logic (updated ~60 fps)

        # Advance puck movement
        self.puck.update()

        # Constrain player striker x-pos to own zone (blue line to right edge)
        if (self.player_striker.position_x <= STRIKER_RADIUS + SCREEN_WIDTH - BLUE_LINE):
            self.player_striker.position_x = STRIKER_RADIUS + SCREEN_WIDTH - BLUE_LINE
        elif (self.player_striker.position_x >= SCREEN_WIDTH - STRIKER_RADIUS):
            self.player_striker.position_x = SCREEN_WIDTH - STRIKER_RADIUS

        # Constrain player striker y-pos inside the board
        if (self.player_striker.position_y <= STRIKER_RADIUS):
            self.player_striker.position_y = STRIKER_RADIUS
        elif (self.player_striker.position_y >= SCREEN_HEIGHT - STRIKER_RADIUS):
            self.player_striker.position_y = SCREEN_HEIGHT - STRIKER_RADIUS

        # Move NPC striker
        self.npc_striker.update(self.puck.position_x, self.puck.position_y)

    def on_key_press(self, key, key_modifiers):
        # Called whenever a key on the keyboard is pressed
        pass

    def on_key_release(self, key, key_modifiers):
        # Called when user releases a previously pressed key
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        # Called whenver the mouse moves
        # Move the center of the player striker to match the mouse x, y
        self.player_striker.position_x = x
        self.player_striker.position_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        # Called when the user presses a mouse button
        print(f"You clicked button number: {button}")

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
