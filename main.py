import time
from typing import Any
import pygame
import soldier
import consts
import screen
import game_field

state: dict[str, Any] = dict()


def main() -> None:
    pygame.init()
    screen.init_screen()
    set_game_state()
    game_field.create_field()
    game_field.create_mines()
    game_field.create_flag()


    while state["is_running"]:
        if time.time() - state["xray_start_time"] > 1:
            state["is_xray"] = False

        handle_user_events()
        if game_field.check_soldier_mine():
            state["state"] = consts.LOSE_STATE
        if game_field.check_soldier_flag():
            state["state"] = consts.WIN_STATE

        print(state["state"])

        screen.draw_game(state)


def set_game_state() -> None:
    global state
    state = {
        "state": consts.RUNNING_STATE,
        "is_running": True,
        "is_xray": False,
        "xray_start_time": time.time(),
    }

def handle_user_events() -> None:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_running"] = False

        elif not state["state"] == consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN and not state["is_xray"]:
                state["is_xray"] = True
                state["xray_start_time"] = time.time()

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