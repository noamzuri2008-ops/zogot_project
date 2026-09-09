import random
import pygame
import consts
import game_field
import soldier


screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

grass_locations: tuple[tuple[int, int]]
grass_image: pygame.Surface
mine_image: pygame.Surface
solider_image: pygame.Surface
night_solider_image: pygame.Surface
flag_image: pygame.Surface

font: pygame.Font

def init_grass_locations() -> None:
    global grass_locations
    end_grass_location = consts.WINDOW_WIDTH - (consts.MINE_COLS * consts.CELL_SIZE)
    grass_locations = tuple(((random.randint(0, end_grass_location), random.randint(0, consts.WINDOW_HEIGHT)) for _ in range(consts.NUM_OF_GRASS)))


def init_images() -> None:
    # grass image
    global grass_image
    grass_image_size = ((consts.MINE_COLS * consts.CELL_SIZE),
                        consts.CELL_SIZE)  # grass image size to fit like mine (3 cols, 1 row)
    original_grass_image = pygame.image.load(consts.GRASS_IMG_PATH).convert_alpha()
    grass_image = pygame.transform.scale(original_grass_image, grass_image_size)

    # mine image
    global mine_image
    mine_image_size = ((consts.MINE_COLS * consts.CELL_SIZE),
                        consts.CELL_SIZE)  # grass image size to fit (3 cols, 1 row)
    original_mine_image =  pygame.image.load(consts.MINE_IMG_PATH).convert_alpha()
    mine_image = pygame.transform.scale(original_mine_image, mine_image_size)

    # soldiers images
    global solider_image
    soldiers_image_size = ((consts.SOLDIER_COLS * consts.CELL_SIZE), (consts.SOLDIER_ROWS * consts.CELL_SIZE))
    original_solider_image = pygame.image.load(consts.SOLIDER_IMG_PATH).convert_alpha()
    solider_image = pygame.transform.scale(original_solider_image, soldiers_image_size)

    global night_solider_image
    original_night_solider_image = pygame.image.load(consts.NIGHT_SOLIDER_IMG_PATH).convert_alpha()
    night_solider_image = pygame.transform.scale(original_night_solider_image, soldiers_image_size)

    # flag image
    global flag_image
    flag_image_size = ((consts.FLAG_WIDTH * consts.CELL_SIZE), (consts.FLAG_HEIGHT * consts.CELL_SIZE))
    original_flag_image = pygame.image.load(consts.FLAG_IMG_PATH)
    flag_image = pygame.transform.scale(original_flag_image, flag_image_size)

def init_fonts() -> None:
    global font
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)

def init_screen() -> None:
    """

    add more inits in this to be run when starting game
    :return: None    :rtype: None
    """
    init_grass_locations()
    init_images()
    init_fonts()


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


def draw_soldier(is_xray: bool) -> None:
    solider_top_matrix, solider_left_matrix = soldier.get_body_locations()[0]
    used_solider_image = solider_image if not is_xray else night_solider_image
    solider_x_screen, solider_y_screen =  solider_left_matrix * consts.CELL_SIZE, solider_top_matrix * consts.CELL_SIZE
    screen.blit(used_solider_image, (solider_x_screen, solider_y_screen))


def draw_grass() -> None:
    for grass_x, grass_y in grass_locations:
        screen.blit(grass_image, (grass_x, grass_y))


def draw_flag() -> None:
    flag_matrix_relative_position_top, flag_matrix_relative_position_left = game_field.flag_locations[0]
    flag_top_matrix, flag_left_matrix = consts.BOARD_ROWS + flag_matrix_relative_position_top, consts.BOARD_COLS + flag_matrix_relative_position_left
    flag_screen_x, flag_screen_y = flag_left_matrix * consts.CELL_SIZE, flag_top_matrix * consts.CELL_SIZE
    screen.blit(flag_image, (flag_screen_x, flag_screen_y))


def draw_mines() -> None:
    for mine_row, mine_col in game_field.mine_matrix_locations[::3]:
        mine_x_screen, mine_y_screen = mine_col * consts.CELL_SIZE, mine_row * consts.CELL_SIZE
        screen.blit(mine_image, (mine_x_screen, mine_y_screen))

def draw_message(message: str, color: tuple[int, int, int], location: tuple[int, int]) -> None:
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def show_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_MESSAGE_COLOR, consts.WIN_MESSAGE_LOCATION)

def show_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_MESSAGE_COLOR, consts.LOSE_MESSAGE_LOCATION)

def draw_game(game_state) -> None:
    draw_background(game_state["is_xray"])

    # xray state - mines or grass
    if game_state["is_xray"]:
        draw_mines()
    else:
        draw_grass()

    draw_flag()
    draw_soldier(game_state["is_xray"])

    if game_state["state"] == consts.WIN_STATE:
        show_win_message()
    elif game_state["state"] == consts.LOSE_STATE:
        show_lose_message()

    pygame.display.update()
