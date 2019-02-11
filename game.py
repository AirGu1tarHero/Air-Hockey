"""
*************************        AIR HOCKEY         ****************************

                             Christopher Dobson
                              15 February 2019
                             CS50 FINAL PROJECT

*******************************************************************************

The Python Arcade library is licensed under the MIT License.
Copyright (c) 2018 Paul Vincent Craven

Permission has been granted to use the Arcade library software according to the
permission notice located at: http://arcade.academy
"""
import arcade
import pymunk
from graphics import *
from physics import *


class Game(arcade.Window):
    # Main application class

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set mouse pointer to disappear inside the window (white background)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WHITE)

        # Initialize the physics space
        self.space = pymunk.Space()
        self.static_lines = physics_space_init(self.space)
        self.space.add(self.static_lines)

        # Create the striker sprite lists
        self.player_striker_list = arcade.SpriteList()
        self.npc_striker_list = arcade.SpriteList()

        # Set up the player
        self.player_body, self.player_shape = create_striker("player", self.player_striker_list)
        self.space.add(self.player_body, self.player_shape)

        # Set up the NPC
        self.npc_body, self.npc_shape = create_striker("npc", self.npc_striker_list)
        self.space.add(self.npc_body, self.npc_shape)

        # Create the puck sprite list
        self.puck_list = arcade.SpriteList()


    def setup(self):
        pass


    def on_draw(self):
        # Render the screen
        arcade.start_render()

        # Draw board
        draw_board()

        # Draw puck and strikers
        self.npc_striker_list.draw()
        self.player_striker_list.draw()
        # self.puck_list.draw()


    def update(self, delta_time):
        # All movement and game logic (updated ~60 fps)
        fps = 60.0
        self.space.step(1 / fps)

        # Move sprites to update with physics object bodies
        move_sprite(self.player_striker_list)


    def on_key_press(self, key, key_modifiers):
        # Called whenever a key on the keyboard is pressed
        pass


    def on_key_release(self, key, key_modifiers):
        # Called when user releases a previously pressed key
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        # Called whenver the mouse moves
        if (x < (SCREEN_WIDTH * 0.7) + STRIKER_RADIUS):
            x = (SCREEN_WIDTH * 0.7) + STRIKER_RADIUS
        elif (x > SCREEN_WIDTH * 0.9):
            x = SCREEN_WIDTH * 0.9

        if (y < STRIKER_RADIUS):
            y = STRIKER_RADIUS
        elif (y > SCREEN_HEIGHT - STRIKER_RADIUS):
            y = SCREEN_HEIGHT - STRIKER_RADIUS

        self.player_body.position = (x, y)

        if (dx == 0 and dy == 0):
            self.player_body.velocity = (0, 0)


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
