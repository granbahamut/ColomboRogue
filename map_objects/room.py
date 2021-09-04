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

    def center(self):
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    def intersect(self, other):
        return self.x1 <= other.x2 \
               and self.x2 >= other.x1 \
               and self.y1 <= other.y2 \
               and self.y2 >= other.y1
