"""
Name:           main.py
Author:         granbahamut
Date:           3/09/2021 10:21 p. m.
Description:    Main script to start the game.
Email:          ivan.dario.pinilla@gmail.com
License:        Apache license 2.0
Version:        0.0.1
"""


import os

import tcod as libtcod
from entity import Entity
from game_map import GameMap
from input_handlers import handle_keys
from render_functions import render_all, clear_all

DATA_FOLDER = "data"
FONT_FILE = os.path.join(DATA_FOLDER, "dejavu10x10_gs_tc.png")


def main():
    """
    Main method to start the game.

    :return:
    """
    print("Welcome to Colombo Rogue!")
    # Screen size
    screen_width = 120
    screen_height = 32
    map_width = 120
    map_height = 32
    room_max_size = 10
    room_min_size = 4
    max_rooms = 10
    screen_title = "My first Roguelike!"

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150)
    }

    # Player coordinates on the map ,and the npc's
    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]
    # Sets the default font settings for the consoles
    libtcod.console_set_custom_font(FONT_FILE, libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, screen_title, False)
    # Add the console to a variable
    con = libtcod.console_new(screen_width, screen_height)
    # Create the map
    game_map = GameMap(map_width, map_height)
    game_map.create_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)

    key = libtcod.Key()
    mouse = libtcod.Mouse()
    # Main loop, where the loop condition is to not have a closing event
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        # Renders and then clears the screen, double buffering applied!
        render_all(con, entities, game_map, screen_width, screen_height, colors)
        libtcod.console_flush()
        clear_all(con, entities)
        # Capture each event to determine the action to follow
        action = handle_keys(key)

        move = action.get('move')
        exit_app = action.get('exit_app')
        fullscreen = action.get('fullscreen')
        # Captured events:
        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)

        if exit_app:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen)


if __name__ == '__main__':
    main()
