"""
Pymunk is a 2D physics library for processing 2D rigid body physics from Python.
It is built on top of the 2D physics library Chipmunk.

2007 - 2018, Victor Blomqvist - vb@viblo.se, MIT License (www.pymunk.org)
"""

import arcade
import pymunk
import math
from graphics import *
from random import randrange

PUCK_RADIUS = int(LINE_WEIGHT * 1.5)
PUCK_MASS = 10
STRIKER_RADIUS = int(PUCK_RADIUS * 2)
STRIKER_MASS = 100

# Define three objects for collision handling
collision_types = {"puck" : 1, "striker" : 2, "goal" : 3}

class CircleSprite(arcade.Sprite):
    """
    The Arcade library handles sprites through the use of lists. This class
    merges Pymunk fuctionality with the Arcade method of creating instances
    of sprite lists.
    """

    def __init__(self, filename, pymunk_shape):
        super().__init__(filename, center_x=pymunk_shape.body.position.x,
                         center_y=pymunk_shape.body.position.y)
        self.width = pymunk_shape.radius * 2
        self.height = pymunk_shape.radius * 2
        self.pymunk_shape = pymunk_shape


def physics_space_init(space):
    # Set the pymunk space and game area boundaries
    static_lines = [
        pymunk.Segment(space.static_body, [50, 0], [SCREEN_WIDTH - 50, 0], 0.0),
        pymunk.Segment(space.static_body, [SCREEN_WIDTH - 50, 0],
                      [SCREEN_WIDTH, 50], 0.0),
        pymunk.Segment(space.static_body, [SCREEN_WIDTH, 50],
                      [SCREEN_WIDTH, BOTTOM_GOAL_POST], 0.0),
        pymunk.Segment(space.static_body, [SCREEN_WIDTH, TOP_GOAL_POST],
                      [SCREEN_WIDTH, SCREEN_HEIGHT - 50], 0.0),
        pymunk.Segment(space.static_body, [SCREEN_WIDTH, SCREEN_HEIGHT - 50],
                      [SCREEN_WIDTH - 50, SCREEN_HEIGHT], 0.0),
        pymunk.Segment(space.static_body, [SCREEN_WIDTH - 50, SCREEN_HEIGHT],
                      [50, SCREEN_HEIGHT], 0.0),
        pymunk.Segment(space.static_body, [50, SCREEN_HEIGHT],
                      [0, SCREEN_HEIGHT - 50], 0.0),
        pymunk.Segment(space.static_body, [0, SCREEN_HEIGHT - 50],
                      [0, TOP_GOAL_POST], 0.0),
        pymunk.Segment(space.static_body, [0, BOTTOM_GOAL_POST], [0, 50], 0.0),
        pymunk.Segment(space.static_body, [0, 50], [50, 0], 0.0)
    ]

    for line in static_lines:
        line.elasticity = 0.95
    return static_lines


def create_striker(name, list):
    # Create the pymunk body
    body = pymunk.Body(STRIKER_MASS, pymunk.inf)
    if (name == "player"):
        x, y = SCREEN_WIDTH - (BLUE_LINE / 2), SCREEN_HEIGHT / 2
    else:
        x, y = BLUE_LINE / 3, SCREEN_HEIGHT / 2
    body.position = (x, y)

    # Define pymunk shape attributes
    shape = pymunk.Circle(body, STRIKER_RADIUS)
    shape.elasticity = 0.9
    shape.collision_type = collision_types["striker"]

    # Add the striker to the respective sprite list
    sprite = CircleSprite("striker.png", shape)
    list.append(sprite)

    return body, shape


def create_puck(list):
    # Create the pymunk body
    body = pymunk.Body(PUCK_MASS, pymunk.inf)
    body.position = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2

    dx = randrange(-300, -100)
    dy = randrange(-300, 300)
    body.apply_impulse_at_local_point(pymunk.Vec2d(dx, dy))

    shape = pymunk.Circle(body, PUCK_RADIUS)
    shape.elasticity = 0.95
    shape.collision_type = collision_types["puck"]

    def constant_velocity(body, gravity, damping, dt):
        body.velocity = body.velocity.normalized() * 700
    body.velocity_func = constant_velocity

    sprite = CircleSprite("puck.png", shape)
    list.append(sprite)

    return body, shape


def move_sprite(list):
    for sprite in list:
        sprite.center_x = sprite.pymunk_shape.body.position.x
        sprite.center_y = sprite.pymunk_shape.body.position.y
        sprite.angle = math.degrees(sprite.pymunk_shape.body.angle)
