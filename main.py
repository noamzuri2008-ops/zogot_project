import time
from typing import Any
import pygame

import save_games
import soldier
import consts
import screen
import game_field

state: dict[str, Any] = dict()
pygame_number_keys: list[int] = [
    pygame.K_1,
    pygame.K_2,
    pygame.K_3,
    pygame.K_4,
    pygame.K_5,
    pygame.K_6,
    pygame.K_7,
    pygame.K_8,
    pygame.K_9,
]

def main() -> None:
    pygame.init()
    screen.init_screen()
    set_game_state()
    game_field.create_field()
    game_field.create_mines()
    game_field.create_flag()

    end_game_timeout: float | int = time.time()

    while state["is_running"]:
        if time.time() - state["xray_start_time"] > 1:
            state["is_xray"] = False

        handle_user_events()
        if game_field.check_soldier_mine():
            state["state"] = consts.LOSE_STATE
        if game_field.check_soldier_flag():
            state["state"] = consts.WIN_STATE

        if state["state"] == consts.RUNNING_STATE:
            end_game_timeout = time.time()
        elif time.time() - end_game_timeout > consts.END_GAME_TIMEOUT:
                break

        screen.draw_game(state)


def set_game_state() -> None:
    global state
    state = {
        "state": consts.RUNNING_STATE,
        "is_running": True,
        "is_xray": False,
        "xray_start_time": time.time(),
        "pressed_loading_saving_num": -1,
        "time_loading_saving_num_pressed" : time.time()

    }


def handle_user_events() -> None:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_running"] = False

        elif not state["state"] == consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN and event.key in pygame_number_keys:
            state["timestamp_loading_saving_num_pressed"] = time.time()
            state["pressed_loading_saving_num"] = event.key

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN and not state["is_xray"]:
                state["is_xray"] = True
                state["xray_start_time"] = time.time()

            if event.key == state["pressed_loading_saving_num"]:
                save_load_num_key_index: int = pygame_number_keys.index(event.key)
                if time.time() - state["timestamp_loading_saving_num_pressed"] > consts.NUM_OF_SECONDS_LOAD_NUM_PRESS:
                    # TODO load game functions
                    # save_games.load_game(save_load_num_key_index)
                    ...
                else:
                    # TODO save game functions
                    # save_games.save_game(save_load_num_key_index)
                    ...

            game_field.remove_soldier()
            if event.key == pygame.K_UP:
                soldier.move_up()
            elif event.key == pygame.K_DOWN:
                soldier.move_down()
            elif event.key == pygame.K_RIGHT:
                soldier.move_right()
            elif event.key == pygame.K_LEFT:
                soldier.move_left()

            game_field.update_solider()


if __name__ == '__main__':
    main()
