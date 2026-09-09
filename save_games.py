
import game_field
import soldier
import screen

def save_game(key):
    data = {
        "soldier leg": soldier.soldier_legs  ,
        "soldier body": soldier.soldier_body ,
        "mines location": game_field.mine_matrix_locations ,
        "grass location": screen.grass_locations
    }

    # TODO save as JSON file
