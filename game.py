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

        # Create the player
        self.player_body, self.player_shape = create_striker("player", self.player_striker_list)
        self.space.add(self.player_body, self.player_shape)

        # Create the NPC
        self.npc_body, self.npc_shape = create_striker("npc", self.npc_striker_list)
        self.space.add(self.npc_body, self.npc_shape)

        # Create the puck sprite list
        self.puck_list = arcade.SpriteList()


    def setup(self):
        # Drop the puck
        self.puck_body, self.puck_shape = create_puck(self.puck_list)
        self.space.add(self.puck_body, self.puck_shape)


    def on_draw(self):
        # Render the screen
        arcade.start_render()

        # Draw board
        draw_board()

        # Draw puck and strikers
        self.npc_striker_list.draw()
        self.player_striker_list.draw()
        self.puck_list.draw()


    def update(self, delta_time):
        # All movement and game logic (updated ~60 fps)
        fps = 60.0
        self.space.step(1 / fps)

        # Get puck and npc striker location
        px, py = self.puck_body.position.x, self.puck_body.position.y
        sy = self.npc_body.position.y

        # NPC body move logic
        if (len(self.puck_list) < 1):
            self.npc_body.position = (BLUE_LINE / 3, SCREEN_HEIGHT / 2)
        else:
            if (px < (SCREEN_WIDTH / 2) and py < sy):
                self.npc_body.velocity = (0, -(SCREEN_HEIGHT / 2))
            elif (px < SCREEN_WIDTH / 2 and py > sy):
                self.npc_body.velocity = (0, (SCREEN_HEIGHT / 2))
            elif (px < BLUE_LINE / 3 or px > SCREEN_WIDTH / 2):
                if (sy < SCREEN_HEIGHT / 2):
                    self.npc_body.velocity = (0, (SCREEN_HEIGHT / 4))
                elif (sy > SCREEN_HEIGHT / 2):
                    self.npc_body.velocity = (0, -(SCREEN_HEIGHT / 4))
                else:
                    self.npc_body.velocity = (0, 0)

        # Move sprites to update with physics object bodies
        move_sprite(self.player_striker_list)
        move_sprite(self.npc_striker_list)

        # Handle puck/goal collision
        for puck in self.puck_list:
            if (px < PUCK_RADIUS and py > BOTTOM_GOAL_POST and py < TOP_GOAL_POST):
                # Remove puck from physics space
                self.space.remove(puck.pymunk_shape, puck.pymunk_shape.body)
                puck.kill()
                # Add to player score
                # TODO
            elif (px > SCREEN_WIDTH - PUCK_RADIUS and py > BOTTOM_GOAL_POST and\
                  py < TOP_GOAL_POST):
                # Remove puck from physics space
                self.space.remove(puck.pymunk_shape, puck.pymunk_shape.body)
                puck.kill()
                # Add to NPC score
                # TODO:
            else:
                move_sprite(self.puck_list)


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
        if (len(self.puck_list) < 1):
            self.setup()


def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
