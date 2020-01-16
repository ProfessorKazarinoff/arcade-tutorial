# window.py
"""
A module which contains the custom arcade Window class
"""

import arcade
import constants

SCREEN_WIDTH = constants.SCREEN_WIDTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
SCREEN_TITLE = constants.SCREEN_TITLE
RADIUS = constants.RADIUS
BACKGROUND_COLOR = constants.BACKGROUND_COLOR
CIRCLE_COLOR = constants.CIRCLE_COLOR

# Custom Window Class


class Welcome(arcade.Window):
    """The main window which appears then the game is run"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, CIRCLE_COLOR
        )
