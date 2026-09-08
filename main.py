from typing import Any
import pygame
import screen


state: dict[str, Any] = dict()


def main() -> None:
    pygame.init()
    screen.init_screen()
    set_game_state()
    while state["is_running"]:
        screen.draw_game(state)


def set_game_state() -> None:
    global state
    state = {
        "is_running": True,
        "is_xray": False,
    }


if __name__ == '__main__':
    main()