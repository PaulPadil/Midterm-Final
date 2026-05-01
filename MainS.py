<<<<<<< HEAD
# main.py

from player import use_item, unequip_item, sell_item, show_inventory, show_stats
from shop import weapon_shop, armour_shop
from save_load import load_game, save_game 


def main_menu():
    while True:
        print("\n=== MENU ===")
        print("1. Weapon Shop")
        print("2. Armour Shop")
        print("3. Inventory")
        print("4. Stats")
        print("5. Equip")
        print("6. Unequip")
        print("7. Sell item")
        print("8. Exit")

        choice = input("Choice: ")

        if choice == "1":
            weapon_shop()

        elif choice == "2":
            armour_shop()

        elif choice == "3":
            show_inventory()

        elif choice == "4":
            show_stats()

        elif choice == "5":
            use_item()

        elif choice == "6":
            unequip_item()

        elif choice == "7":
            sell_item()

        elif choice == "8":
            save_game()

            break


load_game()
=======
# main.py

from player import use_item, unequip_item, sell_item, show_inventory, show_stats
from shop import weapon_shop, armour_shop
from save_load import load_game, save_game 


def main_menu():
    while True:
        print("\033[33m=== MENU ===\033[0m\n")
        print("\033[32m1. Weapon Shop\033[0m")
        print("\033[32m2. Armour Shop\033[0m")
        print("\033[32m3. Inventory\033[0m")
        print("\033[32m4. Stats\033[0m")
        print("\033[32m5. Equip\033[0m")
        print("\033[32m6. Unequip\033[0m")
        print("\033[32m7. Sell item\033[0m")
        print("\033[31m8. Exit\033[0m\n")

        choice = input("\033[33mChoice: \033[0m")

        if choice == "1":
            weapon_shop()

        elif choice == "2":
            armour_shop()

        elif choice == "3":
            show_inventory()

        elif choice == "4":
            show_stats()

        elif choice == "5":
            use_item()

        elif choice == "6":
            unequip_item()

        elif choice == "7":
            sell_item()

        elif choice == "8":
            save_game()

            break


load_game()
>>>>>>> c6675ae (TESTING NI RUSSEL)
main_menu()