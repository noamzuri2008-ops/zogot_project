import consts

soldier_legs = [consts.soldier_legs_row , consts.soldier_left_leg_col , consts.soldier_left_leg_col + 1]
soldier_body = []

def create_body():
    global soldier_body
    for row in range(consts.SOLDIER_BODY_ROWS):
        for col in range(consts.SOLDIER_COLS):
            soldier_body.append((row,col))

create_body()

def get_leg_location():
    global soldier_legs
    return tuple([soldier_legs[0] , soldier_legs[1] , soldier_legs[2]])

def move_up():
    global soldier_legs
    global soldier_body
    soldier_legs[0] += 1
    for item in soldier_body:
        item[0] += 1

def move_down():
    global soldier_legs
    soldier_legs[0] -= 1
    for item in soldier_body:
        item[0] -= 1

def move_left():
    global soldier_legs
    soldier_legs[1] -= 1
    soldier_legs[2] -= 1
    for item in soldier_body:
        item[0]  -= 1

def move_right():
    global soldier_legs
    soldier_legs[1] += 1
    soldier_legs[2] += 1
    for item in soldier_body:
        item[0] += 1
