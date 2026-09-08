import consts
import random
import soldier

field = []
mine_matrix_locations = []
flag_locations = []


def create_field():
    global field
    help1 = []
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            help1.append(consts.EMPTY_TILE)
        field.append(help1)
        help1 = []


def create_mines():
    mine_count = 0
    global mine_matrix_locations
    while mine_count < consts.MINES_COUNT:
        random_row = random.randint(0, consts.BOARD_ROWS - consts.MINE_ROWS)
        random_col = random.randint(0, consts.BOARD_COLS - consts.MINE_COLS)
        if check_availability(random_row, random_col):
            enter_mines_to_matrix(random_row, random_col)
            add_mine_locations_to_list(random_row, random_col)
            mine_count += 1
    return field


def check_availability(row: int, col: int) -> bool:
    return not_flag_solider(row, col) and field[row][col] == field[row][col + 1] == field[row][
        col + 2] == consts.EMPTY_TILE


def not_flag_solider(row1, col1):
    # solider location
    for row in range(consts.SOLDIER_ROWS):
        for col in range(consts.SOLDIER_COLS):
            if row1 == row and col1 == col:
                return False

    # flag location
    for row_flag in range(consts.BOARD_ROWS, consts.FLAG_ROWS, -1):
        for col_flag in range(consts.BOARD_COLS, consts.FLAG_COLS, -1):
            if row_flag == row1 and col_flag == col1:
                return False
    return True


def enter_mines_to_matrix(row, col):
    field[row][col] = consts.MINE
    field[row][col + 1] = consts.MINE
    field[row][col + 2] = consts.MINE


def add_mine_locations_to_list(row, col):
    mine_matrix_locations.append((row, col))
    mine_matrix_locations.append((row, col + 1))
    mine_matrix_locations.append((row, col + 2))


def create_flag():
    global flag_locations
    for row in range(-consts.FLAG_HEIGHT, 0):
        for col in range(-consts.FLAG_WIDTH, 0):
            field[row][col] = consts.FLAG
            flag_locations.append(tuple([row, col]))


def remove_solider():
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == consts.SOLDIER:
                field[row][col] = consts.EMPTY_TILE


def update_solider():
    field[soldier.soldier_legs[0]][soldier.soldier_legs[1]] = consts.SOLDIER
    field[soldier.soldier_legs[0]][soldier.soldier_legs[2]] = consts.SOLDIER
    for item in soldier.soldier_body:
        field[item[0]][item[1]] = consts.SOLDIER


def check_soldier_mine():
    for mine in mine_matrix_locations:
        if mine[0] == soldier.soldier_legs[0] and (
                mine[1] == soldier.soldier_legs[1] or mine[1] == soldier.soldier_legs[2]):
            return True
    return False


def check_soldier_flag():
    for flag in flag_locations:
        for bodypart in soldier.get_body_locations():
            if consts.BOARD_ROWS + flag[0] == bodypart[0] and consts.BOARD_COLS + flag[1] == bodypart[1]:
                return True
    return False


if __name__ == '__main__':
    create_field()
    create_mines()
    [print(row) for row in field]
