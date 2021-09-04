"""
Name:           render_functions.py
Author:         granbahamut
Date:           3/09/2021 10:42 p. m.
Description:    Contains the render functions used to write on console and also clear from console.
Email:          ivan.dario.pinilla@gmail.com
License:        Apache license 2.0
Version:        0.0.1
"""


import tcod as libtcod


def render_all(con, entities, game_map, screen_width, screen_height, colors):
    """Renders every tile on the game map and paints them on the selected console.

    :param con: (console) Console to be painted in.
    :param entities: (Entity[]) a list of entities to paint on the game map.
    :param game_map: (GameMap) map to be used to locate coordinates to paint the tiles and the entities
    :param screen_width: (int) Width of the console.
    :param screen_height: (int) Height of the console.
    :param colors: Colors to be used for each entity, this object defines the foreground/background colors.
    """
    # Draw the map
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.tiles[x][y].block_sight

            if wall:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
    # Draw every entity in thew list provided
    for entity in entities:
        draw_entity(con, entity)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    """Deletes an entity or entities from the specified console

    :param con: (Console) Console to delete the entities.
    :param entities: (Entity[]) Entities to be deleted.
    """
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity):
    """Draws an entity over the specified console.

    :param con: Console to be used to draw.
    :param entity: Entities to be draw.
    """
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)


def clear_entity(con, entity):
    """ Deletes an specific entity from the console.

    :param con: Console to be used to delete.
    :param entity: Entity to be deleted.
    """
    # Erase the character from the console
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)
