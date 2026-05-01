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
>>>>>>> c6675ae (TESTING NI RUSSEL)
main_menu()