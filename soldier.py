import consts
import game_field

soldier_legs = [consts.soldier_legs_row , consts.soldier_left_leg_col , consts.soldier_left_leg_col + 1]
soldier_body = []

def update(new_soldier_legs, new_soldier_body):
    global soldier_legs, soldier_body
    soldier_legs = new_soldier_legs.copy()
    soldier_body = new_soldier_body.copy()

def create_soldier_start():
    for row in range(consts.SOLDIER_ROWS):
        for col in range(consts.SOLDIER_COLS):
            game_field.field[row][col] = consts.SOLDIER

def create_body():
    global soldier_body
    for row in range(consts.SOLDIER_BODY_ROWS):
        for col in range(consts.SOLDIER_COLS):
            soldier_body.append([row,col])

create_body()

def get_leg_location():
    global soldier_legs
    return soldier_legs[0] , soldier_legs[1] , soldier_legs[2]

def get_body_locations() -> list[tuple[int, int]]:
    return soldier_body

def check_up():
    global soldier_body
    if soldier_body[0][0] == 0:
        return False
    return True

def check_down():
    global soldier_legs
    if soldier_legs[0] == consts.BOARD_ROWS - 1:
        return False
    return True

def check_left():
    global soldier_legs
    if soldier_legs[1] == 0:
        return False
    return True

def check_right():
    global soldier_legs
    if soldier_legs[2] == consts.BOARD_COLS - 1:
        return False
    return True

def move_up():
    if check_up():
        global soldier_legs
        global soldier_body
        soldier_legs[0] -= 1
        for item in soldier_body:
            item[0] -= 1


def move_down():
    if check_down():
        global soldier_legs
        soldier_legs[0] += 1
        for item in soldier_body:
            item[0] += 1

def move_left():
    if check_left():
        global soldier_legs
        soldier_legs[1] -= 1
        soldier_legs[2] -= 1
        for item in soldier_body:
            item[1]  -= 1


def move_right():
    if check_right():
        global soldier_legs
        soldier_legs[1] += 1
        soldier_legs[2] += 1
        for item in soldier_body:
            item[1] += 1
