"""
Name:           entity.py
Author:         granbahamut
Date:           3/09/2021 10:16 p. m.
Description:    A generic object to represent everything!.
Email:          ivan.dario.pinilla@gmail.com
License:        Apache license 2.0
Version:        0.0.1
"""


class Entity:
    """Init method"""
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx=0, dy=0):
        """Moves the entity by an amount, defined by dx and dy.

        :param dx: The movement applied on the X axis (default 0)
        :param dy: dy (int): The movement applied on the Y axis (default 0)
        """
        self.x += dx
        self.y += dy
