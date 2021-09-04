"""
Name:           game_map.py
Author:         granbahamut
Date:           4/09/2021 11:06 a. m.
Description:    Map Structure, defines what is a wall or what is not
Email:          ivan.dario.pinilla@gmail.com
License:        Apache license 2.0
Version:        0.0.1
"""
from random import randint
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

    def create_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
        """Creates the map with all of its components

        :param max_rooms: (int) Maximum number of rooms in this dungeon.
        :param room_min_size: (int) Minimum room size.
        :param room_max_size: (int) Maximum room size.
        :param map_width: (int) Map width.
        :param map_height: (int) Map height.
        :param player: (Entity) Player to be put onto the map.
        """
        rooms = []
        num_rooms = 0
        # We create every room with a set of random sizes and random positions:
        for r in range(max_rooms):
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)
            # We create a room with the previous created variables and then check if is a valid room among the others
            # if not, we create a new one.
            new_room = Room(x, y, w, h)

            for other_room in rooms:
                # Invalid room
                if new_room.intersect(other_room):
                    break
            else:
                # Valid room
                self.create_room(new_room)
                (new_x, new_y) = new_room.center()

                if num_rooms == 0:
                    # First room where we add the player
                    player.x = new_x
                    player.y = new_y
                else:
                    # Other rooms goes like this: we go from horizontal to vertical o viceversa to connect them with
                    # a tunnel
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
                    if randint(0, 1) == 1:
                        self.create_hor_tunnel(prev_x, new_x, prev_y)
                        self.create_ver_tunnel(prev_y, new_y, prev_x)
                    else:
                        self.create_ver_tunnel(prev_y, new_y, prev_x)
                        self.create_hor_tunnel(prev_x, new_x, prev_y)

                # Finally, add the room to the array
                rooms.append(new_room)
                num_rooms += 1

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
