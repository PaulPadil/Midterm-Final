# shop.py

import player
from save_load import save_game


def save_item(item_type, item_name, power, price):
    player.inventory.append({
        "type": item_type,
        "name": item_name,
        "power": power,
        "price": price
    })
    save_game()


def weapon_shop():
    weapon_names = ["Sword", "Axe"]
    weapon_prices = [100, 200]
    weapon_attacks = [10, 20]

    while True:
        print("\n=== Weapon Shop ===")
        print("Gold:", player.gold)

        for i in range(len(weapon_names)):
            print(f"{i+1}. {weapon_names[i]} - {weapon_prices[i]} gold")

        print("0. Back")
        choice = input("Choose: ")

        if choice == "0":
            break

        if not choice.isdigit():
            continue

        choice = int(choice)
        index = choice - 1

        if index < 0 or index >= len(weapon_names):
            continue

        if player.gold >= weapon_prices[index]:
            player.gold -= weapon_prices[index]
            save_item("Weapon", weapon_names[index], weapon_attacks[index], weapon_prices[index])
            print("Bought!")
        else:
            print("Not enough gold!")


def armour_shop():
    armour_names = ["Armor", "Heavy Armor"]
    armour_prices = [100, 200]
    armour_def = [10, 20]

    while True:
        print("\n=== Armour Shop ===")
        print("Gold:", player.gold)

        for i in range(len(armour_names)):
            print(f"{i+1}. {armour_names[i]} - {armour_prices[i]} gold")

        print("0. Back")
        choice = input("Choose: ")

        if choice == "0":
            break

        if not choice.isdigit():
            continue

        choice = int(choice)
        index = choice - 1

        if index < 0 or index >= len(armour_names):
            continue

        if player.gold >= armour_prices[index]:
            player.gold -= armour_prices[index]
            save_item("Armour", armour_names[index], armour_def[index], armour_prices[index])
            print("Bought!")
        else:
            print("Not enough gold!")


    