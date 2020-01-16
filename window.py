# window.py
"""
A module which contains the custom arcade Window class
"""

import random
import arcade
import settings
import os
from sprites import Player

SCREEN_WIDTH = settings.SCREEN_WIDTH
SCREEN_HEIGHT = settings.SCREEN_HEIGHT
SCREEN_TITLE = settings.SCREEN_TITLE
RADIUS = settings.RADIUS
BACKGROUND_COLOR = settings.BACKGROUND_COLOR
CIRCLE_COLOR = settings.CIRCLE_COLOR
SCALING = settings.SCALING
MOVEMENT_SPEED = settings.MOVEMENT_SPEED
SPRITE_SCALING = settings.SPRITE_SCALING

# Custom Window Class


class SpaceGame(arcade.Window):
    """The main window which appears then the game is run"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.player_list = None
        self.player_sprite = None
        self.enemies_list = arcade.SpriteList
        self.clouds_list = arcade.SpriteList
        self.all_sprites = arcade.SpriteList

        arcade.set_background_color(arcade.color.AMAZON)

    # def on_draw(self):
    #     arcade.start_render()
    #     arcade.draw_circle_filled(
    #         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, CIRCLE_COLOR
    #     )

    def setup(self):
        """Get game ready to play"""

        self.player_list = arcade.SpriteList()
        # Set up the player
        self.player_sprite = Player(
            ":resources:images/space_shooter/playerShip1_orange.png", SPRITE_SCALING
        )
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """Render the screen"""
        arcade.start_render()

        self.player_list.draw()

    def on_update(self, delta_time: float):
        """Movement and game logic"""
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """Called when a key is pressed"""
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when a key is released"""
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
