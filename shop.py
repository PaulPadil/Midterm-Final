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
    weapon_names = ["\033[32mTsinelas\033[0m", "\033[32mHanger\033[0m", "\033[32mWalis Ting-Ting\033[0m", 
                    "\033[32mPat-Pat\033[0m", "\033[32m2x2\033[0m", "\033[32mSinturon\033[0m"]
    weapon_prices = [50, 100, 130, 150, 200, 250 ]
    weapon_attacks = [10, 20, 50, 85, 105, 130]

    while True:
        print("\n\033[33m=== Weapon Shop ===\033[0m")
        print("\033[33mGold:\033[0m", player.gold)

        for i in range(len(weapon_names)):
            print(f"{i+1}. {weapon_names[i]} - {weapon_prices[i]} \033[33mgold\033[0m {weapon_attacks[i]} \033[31mATK\033[0m")

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
            print("\033[31mNot Enough Pesos!\033[0m")


def armour_shop():
    armour_names = ["\033[32mBlouse\033[0m", "\033[32mPambahay Set\033[0m", "\033[32mPangJogging Set\033[0m",
                    "\033[32mPangGala Set\033[0m","\033[32mValkyrie Set\033[0m","\033[32mSailorMoon\033[0m",]
    armour_prices = [85, 150, 250, 450, 600, 800]
    armour_def = [10, 35, 60, 100, 150, 200]

    while True:
        print("\n\033[33m=== Armor Shop ===\033[0m")
        print("\033[33mGold:\033[0m", player.gold)

        for i in range(len(armour_names)):
            print(f"{i+1}. {armour_names[i]} - {armour_prices[i]} \033[33mgold\033[0m {armour_def[i]} \033[34mDEF\033[0m")

        print("\033[31m0. Back\033[0m")
        choice = input("\033[32mChoose: \033[0m")

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
            print("\033[32mBought!\033[0m")
        else:
            print("\033[31mNot Enough Pesos!\033[0m")


    