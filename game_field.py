import consts
import random

field = []
mine_locations = []
flag_locations = []

def create_field():
    global field
    help = []
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            help.append(consts.EMPTY_TILE)
        field.append(help)
        help = []

def create_mines():
    mine_count = 0
    global mine_locations
    while mine_count< consts.MINES_COUNT:
        random_row = random.randint(0, consts.BOARD_ROWS - consts.MINE_ROWS)
        random_col = random.randint(0, consts.BOARD_COLS - consts.MINE_COLS)
        if check_avaiblity(random_row,random_col):
            enter_mines(random_row, random_col)
            enter_locations(mine_locations,random_row , random_col)
            mine_count += 1
    return field

def create_solider():
    for row in range(consts.SOLDIER_ROWS):
        for col in range(consts.SOLDIER_COLS):
            field[row][col] = consts.SOLDIER

def check_avaiblity(row, col):
    if field[row][col] == consts.EMPTY_TILE and field[row][
        col + 1] == consts.EMPTY_TILE and field[row][
        col + 2] == consts.EMPTY_TILE and not_flag_solider(row , col):
        return True
    return False

def not_flag_solider(row1 , col1):
    for row in range(consts.SOLDIER_ROWS):
        for col in range(consts.SOLDIER_COLS):
            if row1 == row and col1 == col:
                return False
    for row_flag in range(consts.BOARD_ROWS , consts.FLAG_ROWS , -1):
        for col_flag in range(consts.BOARD_COLS , consts.FLAG_COLS , -1):
            if row_flag == row1 and col_flag == col1:
                return False
    return True

def enter_mines(row, col):
    field[row][col] = consts.MINE
    field[row][col + 1] = consts.MINE
    field[row][col + 2] = consts.MINE

def enter_locations(mine_location , row, col):
    mine_location.append(tuple([row,col]))
    mine_location.append(tuple([row ,col+1]))
    mine_location.append(tuple([row ,col+2]))

def create_flag():
    global flag_locations
    for row in range(-consts.FLAG_ROWS, 0):
        for col in range(-consts.FLAG_COLS, 0):
            field[row][col] = consts.FLAG
            flag_locations.append(tuple([row,col]))
