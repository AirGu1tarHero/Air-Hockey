import arcade
from random import randrange as rand

# Set game constants
SCREEN_TITLE = "AIR HOCKEY"

# All board dimensions build off screen width to maintain 16:9 aspect ratio
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = int(SCREEN_WIDTH * 9 / 16)

BLUE_LINE = int(SCREEN_WIDTH * 0.3)
GOAL_ZONE = int(SCREEN_HEIGHT / 2)
GOAL_RADIUS = int(GOAL_ZONE / 2)
GOAL_OFFSET = int(GOAL_RADIUS / 3)
LINE_WEIGHT = int(SCREEN_WIDTH / 100)
DASH_LENGTH = int(LINE_WEIGHT * 2)
FACEOFF_DOT = int(LINE_WEIGHT / 2)

PUCK_RADIUS = int(LINE_WEIGHT * 1.5)
STRIKER_RADIUS = int(PUCK_RADIUS * 2)

def draw_board():
    # Goals
    arcade.draw_circle_outline(-GOAL_OFFSET, SCREEN_HEIGHT / 2, GOAL_RADIUS, \
                               arcade.color.BLUE, LINE_WEIGHT)
    arcade.draw_circle_outline(SCREEN_WIDTH + GOAL_OFFSET, SCREEN_HEIGHT / 2, \
                               GOAL_RADIUS, arcade.color.BLUE, LINE_WEIGHT)
    arcade.draw_rectangle_filled(LINE_WEIGHT, SCREEN_HEIGHT / 2, LINE_WEIGHT * 2,\
                                 GOAL_ZONE, arcade.color.BLACK)
    arcade.draw_rectangle_filled(SCREEN_WIDTH - LINE_WEIGHT, SCREEN_HEIGHT / 2,\
                                 LINE_WEIGHT * 2, GOAL_ZONE, arcade.color.BLACK)

    # Center faceoff circle
    arcade.draw_circle_outline(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, BLUE_LINE / 3,\
                               arcade.color.BLUE, LINE_WEIGHT)
    arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, FACEOFF_DOT,\
                              arcade.color.RED)

    # Center line
    for y in range(0, int((SCREEN_HEIGHT / 2) - (BLUE_LINE / 3)), DASH_LENGTH * 2):
        arcade.draw_line(SCREEN_WIDTH / 2, y, SCREEN_WIDTH / 2, y + DASH_LENGTH, \
                         arcade.color.RED, LINE_WEIGHT)
        arcade.draw_line(SCREEN_WIDTH / 2, SCREEN_HEIGHT - y, SCREEN_WIDTH / 2,\
                         SCREEN_HEIGHT - y - DASH_LENGTH, arcade.color.RED,\
                         LINE_WEIGHT)

    # Blue lines
    arcade.draw_line(BLUE_LINE, 0, BLUE_LINE, SCREEN_HEIGHT, arcade.color.BLUE,\
                     LINE_WEIGHT)
    arcade.draw_line(SCREEN_WIDTH - BLUE_LINE, 0, SCREEN_WIDTH - BLUE_LINE,\
                     SCREEN_HEIGHT, arcade.color.BLUE, LINE_WEIGHT)

    # Corner faceoff circles
    x_pt, y_pt = int(BLUE_LINE / 2), int(SCREEN_HEIGHT / 6)
    for x in range(x_pt, SCREEN_WIDTH, SCREEN_WIDTH - (x_pt * 2)):
        for y in range(y_pt, SCREEN_HEIGHT, SCREEN_HEIGHT - (y_pt * 2)):
            arcade.draw_circle_outline(x, y, x_pt / 2, arcade.color.RED,\
                                       LINE_WEIGHT)
            arcade.draw_circle_filled(x, y, FACEOFF_DOT, arcade.color.RED)

class Puck:
    def __init__(self):
        # Static attributes
        self.position_x = rand(BLUE_LINE, SCREEN_WIDTH - BLUE_LINE)
        self.position_y = SCREEN_HEIGHT / 2
        self.radius = PUCK_RADIUS

        # Dynamic attributes
        self.change_x = 0
        self.change_y = 0

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, \
                                  self.radius, arcade.color.BLACK)
        arcade.draw_circle_outline(self.position_x, self.position_y, \
                                  self.radius - 2, arcade.color.WHITE)

    def drop_puck(self):
        y = rand(2)
        self.change_x = rand(3, 6)
        if (y == 0):
            self.change_y = rand(3, 6)
        else:
            self.change_y = rand(-6, -3)

    def update(self):
        # Move the puck
        self.position_x += self.change_x
        self.position_y += self.change_y

        # Bounce when reaching edge of board
        if self.position_x < self.radius:
            self.change_x *= -1
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1
        if self.position_y < self.radius:
            self.change_y *= -1
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1

        # Check for collision with striker and change direction if required
        # if (self.position_x > SCREEN_WIDTH / 2):
        #     collision_check(self.position_x, self.position_y, self.radius,\
        #                     player_striker_x, player_striker_y, STRIKER_RADIUS)
        # else:
        #     collision_check(self.position_x, self.position_y, self.radius,\
        #                     npc_striker_x, npc_striker_y, STRIKER_RADIUS)

class Striker:
    def __init__(self, position_x, position_y, radius):
        # Static attributes
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.glint = radius / 10

        # Dynamic attributes (for NPC)
        # self.change_x = 0 ... (code reserved for future use)
        self.change_y = 0

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, \
                                  self.radius, arcade.color.RED)
        arcade.draw_circle_outline(self.position_x, self.position_y, \
                                   self.radius, arcade.color.BLACK, LINE_WEIGHT)
        arcade.draw_circle_outline(self.position_x, self.position_y, \
                                   self.radius / 2, arcade.color.BLACK, LINE_WEIGHT)
        arcade.draw_circle_filled(self.position_x, self.position_y, \
                                  self.radius * 0.8, (0, 0, 0, 20))
        arcade.draw_circle_filled(self.position_x, self.position_y, \
                                  self.radius * 0.7, (0, 0, 0, 40))
        arcade.draw_circle_filled(self.position_x + self.glint, self.position_y +\
                                  self.glint, self.radius * 0.1, (255, 255, 255, 180))
        arcade.draw_circle_filled(self.position_x + self.glint, self.position_y +\
                                  self.glint, self.radius * 0.05, arcade.color.WHITE)

    def update(self, puck_x, puck_y):
        # Move the NPC striker
        # self.position_x += self.change_x ... (code reserved for future use)

        if (puck_x < SCREEN_WIDTH / 2):
            self.change_y = 3
        else:
            self.change_y = 1

        y_pt = SCREEN_HEIGHT / 6
        if (puck_y > self.position_y):
            if (self.position_y > SCREEN_HEIGHT - y_pt):
                self.position_y = SCREEN_HEIGHT - y_pt
            else:
                self.position_y += self.change_y
        else:
            if (self.position_y < y_pt):
                self.position_y = y_pt
            else:
                self.position_y -= self.change_y
