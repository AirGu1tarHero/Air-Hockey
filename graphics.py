import arcade

# Set game constants
SCREEN_TITLE = "AIR HOCKEY"
SCREEN_WIDTH = 1000

# All board dimensions build off screen width to maintain 16:9 aspect ratio
SCREEN_HEIGHT = int(SCREEN_WIDTH * 9 / 16)

BLUE_LINE = int(SCREEN_WIDTH * 0.3)
GOAL_ZONE = int(SCREEN_HEIGHT / 2)
GOAL_RADIUS = int(GOAL_ZONE / 2)
GOAL_OFFSET = int(GOAL_RADIUS / 3)
BOTTOM_GOAL_POST = int((SCREEN_HEIGHT /2) - (GOAL_ZONE / 2))
TOP_GOAL_POST = int((SCREEN_HEIGHT /2) + (GOAL_ZONE / 2))
LINE_WEIGHT = int(SCREEN_WIDTH / 100)
DASH_LENGTH = int(LINE_WEIGHT * 2)
FACEOFF_DOT = int(LINE_WEIGHT / 2)


def draw_board(npc_score, player_score):
    # Goals
    arcade.draw_circle_outline(-GOAL_OFFSET, SCREEN_HEIGHT / 2, GOAL_RADIUS,
                               arcade.color.BLUE, LINE_WEIGHT)
    arcade.draw_circle_outline(SCREEN_WIDTH + GOAL_OFFSET, SCREEN_HEIGHT / 2,
                               GOAL_RADIUS, arcade.color.BLUE, LINE_WEIGHT)
    arcade.draw_rectangle_filled(LINE_WEIGHT, SCREEN_HEIGHT / 2, LINE_WEIGHT * 2,
                                 GOAL_ZONE, arcade.color.BLACK)
    arcade.draw_rectangle_filled(SCREEN_WIDTH - LINE_WEIGHT, SCREEN_HEIGHT / 2,
                                 LINE_WEIGHT * 2, GOAL_ZONE, arcade.color.BLACK)

    # Center faceoff circle
    arcade.draw_circle_outline(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, BLUE_LINE / 3,
                               arcade.color.BLUE, LINE_WEIGHT)
    arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, FACEOFF_DOT,
                              arcade.color.RED)

    # Center line
    for y in range(0, int((SCREEN_HEIGHT / 2) - (BLUE_LINE / 3)), DASH_LENGTH * 2):
        arcade.draw_line(SCREEN_WIDTH / 2, y, SCREEN_WIDTH / 2, y + DASH_LENGTH,
                         arcade.color.RED, LINE_WEIGHT)
        arcade.draw_line(SCREEN_WIDTH / 2, SCREEN_HEIGHT - y, SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT - y - DASH_LENGTH, arcade.color.RED,
                         LINE_WEIGHT)

    # Blue lines
    arcade.draw_line(BLUE_LINE, 0, BLUE_LINE, SCREEN_HEIGHT, arcade.color.BLUE,
                     LINE_WEIGHT)
    arcade.draw_line(SCREEN_WIDTH - BLUE_LINE, 0, SCREEN_WIDTH - BLUE_LINE,
                     SCREEN_HEIGHT, arcade.color.BLUE, LINE_WEIGHT)

    # Corner faceoff circles
    x_pt, y_pt = int(BLUE_LINE / 2), int(SCREEN_HEIGHT / 6)
    for x in range(x_pt, SCREEN_WIDTH, SCREEN_WIDTH - (x_pt * 2)):
        for y in range(y_pt, SCREEN_HEIGHT, SCREEN_HEIGHT - (y_pt * 2)):
            arcade.draw_circle_outline(x, y, x_pt / 2, arcade.color.RED,
                                       LINE_WEIGHT)
            arcade.draw_circle_filled(x, y, FACEOFF_DOT, arcade.color.RED)

    # Draw corners
    arcade.draw_polygon_filled(((SCREEN_WIDTH - 50, 0),
                                (SCREEN_WIDTH, 50), (SCREEN_WIDTH, 0)),
                                arcade.color.BLACK)
    arcade.draw_polygon_filled(((SCREEN_WIDTH, SCREEN_HEIGHT - 50),
                                (SCREEN_WIDTH - 50, SCREEN_HEIGHT),
                                (SCREEN_WIDTH, SCREEN_HEIGHT)),
                                arcade.color.BLACK)
    arcade.draw_polygon_filled(((50, SCREEN_HEIGHT), (0, SCREEN_HEIGHT - 50),
                                (0, SCREEN_HEIGHT)), arcade.color.BLACK)
    arcade.draw_polygon_filled(((0, 50), (50, 0), (0, 0)), arcade.color.BLACK)

    # Draw score
    output = f"NPC Score: {npc_score}"
    arcade.draw_text(output, 400, 550, arcade.color.BLACK, 14)

    output = f"Player Score: {player_score}"
    arcade.draw_text(output, 600, 550, arcade.color.BLACK, 14)
