"""
Name:           render_functions.py
Author:         
Date:           3/09/2021 10:42 p. m.
Description:    Contains the render functions used to write on console and also clear from console.
Email:          ivan.dario.pinilla@gmail.com
License:        Apache license 2.0
Version:        0.0.1
"""


import tcod as libtcod


def render_all(con, entities, screen_width, screen_height):
    # Draw every entity in thew list provided
    for entity in entities:
        draw_entity(con, entity)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)


def clear_entity(con, entity):
    # Erase the character from the console
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)
