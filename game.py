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

# Define game states
PAUSED = 0
ACTION = 1

class Game(arcade.Window):
    # Main application class

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set starting game state
        self.game_state = PAUSED

        # Set mouse pointer to disappear inside the window (white background)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WHITE)

        # Initialize the physics space
        self.space = pymunk.Space()
        self.static_lines = physics_space_init(self.space)
        self.space.add(self.static_lines)

        # Initialize sprite lists
        self.player_striker_list = None
        self.npc_striker_list = None
        self.puck_list = None

        # Generate sprite lists
        self.player_striker_list = arcade.SpriteList()
        self.npc_striker_list = arcade.SpriteList()
        self.puck_list = arcade.SpriteList()

        # Create the player
        self.player_body, self.player_shape = create_striker("player", self.player_striker_list)
        self.space.add(self.player_body, self.player_shape)
        self.player_score = 0

        # Create the NPC
        self.npc_body, self.npc_shape = create_striker("npc", self.npc_striker_list)
        self.space.add(self.npc_body, self.npc_shape)
        self.npc_score = 0


    def setup(self):
        # Create the puck
        self.puck_body, self.puck_shape = create_puck(self.puck_list)
        self.space.add(self.puck_body, self.puck_shape)


    def draw_game_paused(self):
        # Draw board
        draw_board(self.npc_score, self.player_score)

        output = "Air Hockey"
        arcade.draw_text(output, 240, 400, arcade.color.BLACK, 54)

        output = "Click Mouse to Start"
        arcade.draw_text(output, 310, 300, arcade.color.BLACK, 24)

        output = "Press <Cmd-Q> to Quit"
        arcade.draw_text(output, 310, 250, arcade.color.BLACK, 24)

    def draw_game_action(self):
        # Draw board
        draw_board(self.npc_score, self.player_score)

        # Draw puck and strikers
        self.npc_striker_list.draw()
        self.player_striker_list.draw()
        self.puck_list.draw()


    def on_draw(self):
        # Render the screen
        arcade.start_render()

        if (self.game_state == PAUSED):
            self.draw_game_paused()
        elif (self.game_state == ACTION):
            self.draw_game_action()


    def update(self, delta_time):
        # Only update if game state is ACTION
        if self.game_state == ACTION:
            # All movement and game logic (updated ~60 fps)
            fps = 60.0
            self.space.step(1 / fps)

            # Get puck and npc striker location
            px, py = self.puck_body.position.x, self.puck_body.position.y
            sy = self.npc_body.position.y

            # NPC body move logic
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
                    self.player_score += 1
                    self.pause_game()
                elif (px > SCREEN_WIDTH - PUCK_RADIUS and py > BOTTOM_GOAL_POST and\
                      py < TOP_GOAL_POST):
                    # Remove puck from physics space
                    self.space.remove(puck.pymunk_shape, puck.pymunk_shape.body)
                    puck.kill()
                    # Add to NPC score
                    self.npc_score += 1
                    self.pause_game()
                else:
                    move_sprite(self.puck_list)

    def pause_game(self):
        # Set game state to PAUSE and reset NPC striker
        self.game_state = PAUSED
        self.npc_body.position = (BLUE_LINE / 3, SCREEN_HEIGHT / 2)
        self.npc_body.velocity = (0, 0)

    def on_mouse_motion(self, x, y, dx, dy):
        # Called whenver the mouse moves while game active
        if self.game_state == ACTION:
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
        if self.game_state == PAUSED:
            self.setup()
            self.game_state = ACTION


def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
