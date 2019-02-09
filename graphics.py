import arcade, random

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

class Puck:
    def __init__(self, position_x, position_y, radius):
        # Static attributes
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius

        # Dynamic attributes
        self.change_x = 0
        self.change_y = 0

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, \
                                  self.radius, arcade.color.BLACK)
        arcade.draw_circle_outline(self.position_x, self.position_y, \
                                  self.radius - 2, arcade.color.WHITE)

    def drop_puck(self):
        # Position the coin
        self.position_x = random.randrange(1000)
        self.position_y = random.randrange(600)
        self.change_x = random.randrange(-5, -3)
        self.change_y = random.randrange(-5, 5)

    def update(self):
        # Move the puck
        self.position_x += self.change_x
        self.position_y += self.change_y

        # Bounce when reaching edge of board
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > 1000 - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > 600 - self.radius:
            self.change_y *= -1

class Striker:
    def __init__(self, position_x, position_y, radius):
        # Static attributes
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius

        # Dynamic attributes (for NPC)
        # self.change_x = 0 ... (code reserved for future use)
        self.change_y = 0

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, \
                                  self.radius, arcade.color.RED)
        arcade.draw_circle_outline(self.position_x, self.position_y, \
                                  self.radius, arcade.color.BLACK, 10)
        arcade.draw_circle_outline(self.position_x, self.position_y, \
                                  self.radius / 2, arcade.color.BLACK, 10)
        arcade.draw_circle_filled(self.position_x, self.position_y, \
                                  self.radius * 0.8, (0, 0, 0, 20))
        arcade.draw_circle_filled(self.position_x, self.position_y, \
                                  self.radius * 0.7, (0, 0, 0, 40))
        arcade.draw_circle_filled(self.position_x + 3, self.position_y + 4, \
                                  self.radius * 0.1, (255, 255, 255, 180))
        arcade.draw_circle_filled(self.position_x + 3, self.position_y + 4, \
                                  self.radius * 0.05, arcade.color.WHITE)

    def update(self, puck_x, puck_y):
        # Move the NPC striker
        # self.position_x += self.change_x ... (code reserved for future use)

        if (puck_x < 500):
            self.change_y = 3
        else:
            self.change_y = 1

        if (puck_y > self.position_y):
            if (self.position_y > 500):
                self.position_y = 500
            else:
                self.position_y += self.change_y
        else:
            if (self.position_y < 100):
                self.position_y = 100
            else:
                self.position_y -= self.change_y
