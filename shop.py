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
    weapon_names = ["\033[32mWoodenSword\033[0m", "\033[32mIron Sword\033[0m", 
                    "\033[32mBuster Blade\033[0m", "\033[32mWarhammer\033[0m",
                    "\033[32mDemon Slayer\033[0m"]
    weapon_prices = [45, 75, 150, 350, 500]
    weapon_attacks = [10, 25, 50, 100, 185 ]

    while True:
        print("\n\033[33m=== Weapon Shop ===\033[0m")
        print("\033[33mGold:\033[0m", player.gold)

        for i in range(len(weapon_names)):
            print(f"{i+1}. {weapon_names[i]} - ({weapon_prices[i]} \033[33mgold\033[0m) ({weapon_attacks[i]} \033[31mATK\033[0m)")

        print("\033[31m0. Back\033[0m")
        choice = input("\033[32mChoose: \033[0m")

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
            print("\033[33mBought!\033[0m")
        else:
            print("\033[31mNot enough gold!\033[0m")


def armour_shop():
    armour_names = ["Leather armor", "Knights armor","Oblivion", "Juggernaut","Abyssal Knight"]
    armour_prices = [75, 125, 300, 500, 850]
    armour_def = [10, 50, 85, 120, 185 ]

    while True:
        print("\033[33m=== Armour Shop ===\033[0m")
        print("\033[33mGold:\033[0m", player.gold)

        for i in range(len(armour_names)):
            print(f"{i+1}. {armour_names[i]} - ({armour_prices[i]} \033[33mgold\033[0m) ({armour_def[i]} \033[34mDef\033[0m)")

        print("\033[31m0. Back\033[0m")
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
            print("\033[33mBought!\033[0m")
        else:
            print("\033[31mNot enough gold!\033[0m")