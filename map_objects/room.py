"""
Name:           room.py
Author:         granbahamut
Date:           4/09/2021 11:41 a. m.
Description:    Defines the rules to create a Room
Email:          ivan.dario.pinilla@gmail.com
License:        Apache license 2.0
Version:        0.0.1
"""


class Room:
    def __init__(self, x_pos, y_pos, width, height):
        """Defines the dimensions of the room and it's position

        :param x_pos: (int) Position on the x axis of the map.
        :param y_pos: (int) Position on the y axis of the map.
        :param width: (int) width of the map.
        :param height: (int) height of the map.
        """
        self.x1 = x_pos
        self.y1 = y_pos
        self.x2 = x_pos + width
        self.y2 = y_pos + height
