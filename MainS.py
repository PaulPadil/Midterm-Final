# main.py

from player import use_item, unequip_item, sell_item, show_inventory, show_stats
from shop import weapon_shop, armour_shop
from save_load import load_game, save_game 


def main_menu():
    while True:
        print("\n\033[33m=== Shop Menu ===\033[0m\n")
        print("\033[32m1. Weapon Shop\033[0m")
        print("\033[32m2. Armour Shop\033[0m")
        print("\033[32m3. Inventory\033[0m")
        print("\033[32m4. Use / Consume Item\033[0m")
        print("\033[32m5. Unequip Item\033[0m")
        print("\033[32m6. Sell Item\033[0m")
        print("\033[32m7. Statistics\033[0m")
        print("\033[31m8. Exit\033[0m\n")

        choice = input("\033[32mChoose: \033[0m")

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("\033[31mInvalid choice! Please choose a number from 1 to 8c.\033[0m")
            continue

        if choice == "1":
            weapon_shop()

        elif choice == "2":
            armour_shop()

        elif choice == "3":
            show_inventory()

        elif choice == "4":
            use_item()

        elif choice == "5":
            unequip_item()

        elif choice == "6":
            sell_item()

        elif choice == "7":
            show_stats()

        elif choice == "8":
            save_game()

            break


load_game()
main_menu()