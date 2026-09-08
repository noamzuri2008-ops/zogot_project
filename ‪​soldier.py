import game_field
import consts


def start_location():
    game_field.create_soldier()

def leg_location():
    leg_loc = []
    for row in range(len(game_field.field)):
        for col in range(len(game_field.field[row])):
            if check_leg(row, col):
                leg_loc.append([row, col])

def check_leg (row, col):
    if game_field.field[row][col] == consts.SOLDIER and game_field.field[row + 1][
        col] == consts.SOLDIER and game_field.field[row + 2][
        col] == consts.SOLDIER:
        return True
    return False