# player.py

gold = 1000
base_attack = 10
base_defense = 5

equipped_weapon = None
equipped_armour = None
inventory = []


def show_inventory():
    print("\n\033[32m=== Inventory ===\033[0m")

    if len(inventory) == 0:
        print("\033[32mNo items in inventory.\033[0m")
    else:
        for i, item in enumerate(inventory):
            if item["type"] == "Weapon":
                print(f"{i+1}. {item['name']} (ATK +{item['power']}, Price {item['price']})")
            elif item["type"] == "Armour":
                print(f"{i+1}. {item['name']} (DEF +{item['power']}, Price {item['price']})")


def show_stats():
    weapon_attack = equipped_weapon["power"] if equipped_weapon else 0
    armour_defense = equipped_armour["power"] if equipped_armour else 0

    total_attack = base_attack + weapon_attack
    total_defense = base_defense + armour_defense

    print("\n\033[33m=== Statistik Ni Nanay ===\033[0m")
    print("\033[33mGold: \033[0m", gold)
    print("\033[31mTotal Attack: \033[0m", total_attack)
    print("\033[34mTotal Defense: \033[0m", total_defense)

def use_item():
    global equipped_weapon, equipped_armour

    if len(inventory) == 0:
        print("\033[32mNo items in inventory. Nothing to use.\033[0m")
        return

    show_inventory()
    choice = input("\033[32mChoose an item to use (0 to cancel): \033[0m")

    if choice == "0":
        
        return
         

    if not choice.isdigit():
        print("\033[31mInvalid choice!\033[0m")
        return

    choice = int(choice)

    if choice < 1 or choice > len(inventory):
        print("\033[31mInvalid choice!\033[0m")
        return

    item = inventory[choice - 1]

    if item["type"] == "Weapon":
        equipped_weapon = item
        print(f"Equipped {item['name']} (ATK +{item['power']})")

    elif item["type"] == "Armour":
        equipped_armour = item
        print(f"Equipped {item['name']} (DEF +{item['power']})")

def unequip_item():
    global equipped_weapon, equipped_armour

    while True:
        print("\n\033[0m=== Unequip an item ===\033[0m")
        print("\033[32m1. Unequip Weapon \033[0m")
        print("\033[32m2. Unequip Armour \033[0m")
        print("\033[32m3. Unequip All \033[0m")
        print("\033[32m0. Back \033[0m")
        choice = input("\033[32mChoose: \033[0m")

        if choice == "1":
            if equipped_weapon:
                print(f"{equipped_weapon['name']} has been unequipped.")
                equipped_weapon = None
            else:
                print("\033[32mNo weapon equipped.\033[0m")

        elif choice == "2":
            if equipped_armour:
                print(f"{equipped_armour['name']} has been unequipped.")
                equipped_armour = None
            else:
                print("\033[32mNo armour equipped.\033[0m")

        elif choice == "3":
            equipped_weapon = None
            equipped_armour = None
            print("\033[32mAll items have been unequipped.\033[0m")

        elif choice == "0":
            break

        else:
            print("\033[31mInvalid choice!.\033[0m")
            
def sell_item():
    global gold, equipped_weapon, equipped_armour

    if len(inventory) == 0:
        print("\033[32mNo items in inventory. Nothing to sell.\033[0m")
        return

    show_inventory()
    choice = input("\033[32mChoose an item to sell (0 to cancel): \033[0m")

    if choice == "0":
        return

    if not choice.isdigit():
        print("\033[31mInvalid choice!\033[0m")
        return

    choice = int(choice)

    if choice < 1 or choice > len(inventory):
        print("\033[31mInvalid item number!.\033[0m")
        return

    item = inventory[choice - 1]

    # Prevent selling equipped items
    if equipped_weapon is not None and item == equipped_weapon:
        print("\033[31mYou cannot sell equipped Weapon. Please unequip it first. \033[0m")
        return

    if equipped_armour is not None and item == equipped_armour:
        print("\033[31mYou cannot sell equipped Armour. Please unequip it first. \033[0m")
        return

    sell_price = item["price"] // 2
    gold += sell_price

    sold_item = inventory.pop(choice - 1)

    print(f"\033[32mYou sold {sold_item['name']} for {sell_price} Gold!\033[0m")
    print("\033[33mGold:\033[0m", gold)