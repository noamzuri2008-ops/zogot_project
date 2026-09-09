import json
import os

import game_field
import soldier
import screen
import consts

data = {
    "soldier leg": soldier.soldier_legs,
    "soldier body": soldier.soldier_body,
    "mines location": game_field.mine_matrix_locations,
    "grass location": list()
}

def save_game(save_file_index) -> None:
    path = consts.SAVING_FILES_PATH.format(key=save_file_index)
    update_data()
    with open(path, "w") as f:
        json.dump(data, f)

def pull_game(path):
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)

def update_data():
    global data
    data = {
        "soldier leg": soldier.soldier_legs,
        "soldier body": soldier.soldier_body,
        "mines location": game_field.mine_matrix_locations,
        "grass location": screen.grass_locations
    }




