"""
Name:           game_map.py
Author:         granbahamut
Date:           4/09/2021 11:06 a. m.
Description:    Map Structure, defines what is a wall or what is not
Email:          ivan.dario.pinilla@gmail.com
License:        Apache license 2.0
Version:        0.0.1
"""
from map_objects.room import Room
from map_objects.tile import Tile


class GameMap:
    def __init__(self, width, height):
        """Defines dimensions of a map

        :param width: (int) width of the map.
        :param height: (int) height of the map.
        """
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        """Sets the tiles to blockable = true, so every tile is not passable

        :return:
        """
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def create_map(self):
        """Creates the map with all of its components

        """
        room1 = Room(20, 15, 10, 15)
        room2 = Room(35, 15, 10, 15)

        self.create_room(room1)
        self.create_room(room2)

        self.create_hor_tunnel(25, 40, 23)

    def create_room(self, room):
        """Creates a room based on a rectangular shape given by the room argument.

        :param room: The room dimensions in a room object
        """
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_hor_tunnel(self, x1, x2, y):
        """Adds a horizontal tunnel to connect two rooms

        :param x1: (int) Starting point on the X axis.
        :param x2: (int) Ending point on the X axis.
        :param y: (int) Starting point on the Y axis.
        """
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_ver_tunnel(self, y1, y2, x):
        """Adds a vertical tunnel to connect two rooms

        :param x1: (int) Starting point on the Y axis.
        :param x2: (int) Ending point on the Y axis.
        :param y: (int) Starting point on the X axis.
        """
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        """Checks is a Tile can block a player or not

        :param x: (int) X position of the tile.
        :param y: (int) X position of the tile.
        :return: True if it blocks a player, false otherwise
        """
        if self.tiles[x][y].blocked:
            return True
        return False
