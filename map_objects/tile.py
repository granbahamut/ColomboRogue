"""
Name:           tile.py
Author:         granbahamut
Date:           3/09/2021 10:56 p. m.
Description:    This script contains the base definition of a Tile object
Email:          ivan.dario.pinilla@gmail.com
License:        Apache license 2.0
Version:        0.0.1
"""


class Tile:
    """Defines a tile on a map, and defines if is blocked and if can block sight."""
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
        # Blocked tiles also block sight, like a wall!
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
