
# save_load.py

import json
import player


def save_game():
    data = {
        "gold": player.gold,
        "inventory": player.inventory,
        "equipped_weapon": player.equipped_weapon,
        "equipped_armour": player.equipped_armour
    }

    with open("save_data.json", "w") as file:
        json.dump(data, file)


def load_game():
    try:
        with open("save_data.json", "r") as file:
            data = json.load(file)

            player.gold = data["gold"]
            player.inventory = data["inventory"]
            player.equipped_weapon = data["equipped_weapon"]
            player.equipped_armour = data["equipped_armour"]

    except FileNotFoundError:
        print("\033[32mNo save file found. Starting new game.\033[0m")


# save_load.py

import json
import player


def save_game():
    data = {
        "gold": player.gold,
        "inventory": player.inventory,
        "equipped_weapon": player.equipped_weapon,
        "equipped_armour": player.equipped_armour
    }

    with open("save_data.json", "w") as file:
        json.dump(data, file)


def load_game():
    try:
        with open("save_data.json", "r") as file:
            data = json.load(file)

            player.gold = data["gold"]
            player.inventory = data["inventory"]
            player.equipped_weapon = data["equipped_weapon"]
            player.equipped_armour = data["equipped_armour"]

    except FileNotFoundError:
        print("\033[32mNo save file found. Starting new game.\033[0m")


