import arcade

def draw_board():
    # Goals
    arcade.draw_circle_outline(-50, 300, 150, arcade.color.BLUE, 10)
    arcade.draw_circle_outline(1050, 300, 150, arcade.color.BLUE, 10)
    arcade.draw_rectangle_filled(10, 300, 20, 300, arcade.color.BLACK)
    arcade.draw_rectangle_filled(990, 300, 20, 300, arcade.color.BLACK)

    # Center circle
    arcade.draw_circle_outline(500, 300, 100, arcade.color.BLUE, 10)
    arcade.draw_circle_filled(500, 300, 5, arcade.color.RED)

    # Center line
    for y in range(10, 210, 40):
        arcade.draw_line(500, y, 500, y + 20, arcade.color.RED, 10)
        arcade.draw_line(500, y + 400, 500, y + 420, arcade.color.RED, 10)

    # Blue lines
    arcade.draw_line(300, 0, 300, 600, arcade.color.BLUE, 10)
    arcade.draw_line(700, 0, 700, 600, arcade.color.BLUE, 10)

    # Corner circles
    for x in range(150, 851, 700):
        for y in range(100, 501, 400):
            arcade.draw_circle_outline(x, y, 75, arcade.color.RED, 10)
            arcade.draw_circle_filled(x, y, 5, arcade.color.RED)
