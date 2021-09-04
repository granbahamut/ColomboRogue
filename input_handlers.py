"""
Name:           input_handlers.py
Author:         granbahamut
Date:           3/09/2021 10:18 p. m.
Description:    Controls the keyboard events.
Email:          ivan.dario.pinilla@gmail.com
License:        Apache license 2.0
Version:        0.0.1
"""


import tcod as libtcod


def handle_keys(key):
    """Defines the actions for each key present on the game.

    :param key: Defines the key event received
    :return:
    """
    # Movement Keys
    if key.vk == libtcod.KEY_UP:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move': (1, 0)}
    # Toggle fullscreen
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    # Exit the game
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit_app': True}
    # no key pressed
    return {}
