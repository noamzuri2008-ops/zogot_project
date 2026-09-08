import random
import pygame
import consts

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

grass_locations: tuple[tuple[int, int]]
grass_image: pygame.Surface


def init_grass() -> None:
    global grass_locations
    end_grass_location = consts.WINDOW_WIDTH - (consts.MINE_COLS * consts.CELL_SIZE)
    grass_locations = tuple(((random.randint(0, end_grass_location), random.randint(0, consts.WINDOW_HEIGHT)) for _ in range(consts.NUM_OF_GRASS)))


def init_images() -> None:
    global grass_image
    grass_image_size = ((consts.MINE_COLS * consts.CELL_SIZE),
                        consts.CELL_SIZE)  # grass image size to fit (3 cols, 1 row)
    original_grass_image = pygame.image.load(consts.GRASS_IMG_PATH).convert_alpha()
    grass_image = pygame.transform.scale(original_grass_image, grass_image_size)


def init_screen() -> None:
    init_grass()
    init_images()
    # add more screen inits in this to be run when starting game


def draw_xray_lines() -> None:
    # horizontal lines
    for row_index in range(consts.BOARD_ROWS + 1):
        horizontal_line_start_pos = (0, row_index * consts.CELL_SIZE)
        horizontal_line_end_pos = (consts.WINDOW_WIDTH, row_index * consts.CELL_SIZE)
        pygame.draw.line(screen, consts.XRAY_LINE_COLOR, horizontal_line_start_pos, horizontal_line_end_pos,
                         consts.XRAY_LINE_WIDTH)

    # vertical lines
    for col_index in range(consts.BOARD_COLS + 1):
        vertical_line_start_pos = (col_index * consts.CELL_SIZE, 0)
        vertical_line_end_pos = (col_index * consts.CELL_SIZE, consts.WINDOW_HEIGHT)
        pygame.draw.line(screen, consts.XRAY_LINE_COLOR, vertical_line_start_pos, vertical_line_end_pos,
                         consts.XRAY_LINE_WIDTH)


def draw_background(is_xray: bool) -> None:
    if is_xray:
        screen.fill(consts.BACKGROUND_COLOR_XRAY)
        draw_xray_lines()
    else:
        screen.fill(consts.BACKGROUND_COLOR)


def draw_soldier() -> None:
    # TODO draw soldier
    ...


def draw_grass() -> None:
    global grass_image
    global grass_locations
    for grass_x, grass_y in grass_locations:
        screen.blit(grass_image, (grass_x, grass_y))


def draw_flag() -> None:
    # TODO draw flag
    ...

def draw_mines() -> None:
    # TODO draw mines
    ...

def draw_game(game_state) -> None:
    draw_background(game_state["is_xray"])

    # xray state not having grass
    if not game_state["is_xray"]:
        draw_grass()
    else:
        draw_mines()

    pygame.display.update()
