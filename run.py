# run.py

"""
basic running script to run the game.

From the command line

 > python run.py

"""

import arcade
from window import Welcome


def main():
    app = Welcome()
    arcade.run()


if __name__ == "__main__":
    main()
