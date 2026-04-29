# player.py

gold = 1000
base_attack = 10
base_defense = 5

equipped_weapon = None
equipped_armour = None
inventory = []


def show_inventory():
    print("\n=== Inventory ===")

    if len(inventory) == 0:
        print("Inventory is empty.")
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

    print("\n=== Player Stats ===")
    print("Gold:", gold)
    print("Total Attack:", total_attack)
    print("Total Defense:", total_defense)

def use_item():
    global equipped_weapon, equipped_armour

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    show_inventory()
    choice = input("Choose item number to equip (0 to cancel): ")

    if choice == "0":
        
        return
         

    if not choice.isdigit():
        print("Invalid input!")
        return

    choice = int(choice)

    if choice < 1 or choice > len(inventory):
        print("Invalid choice.")
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
        print("\n=== Unequip Menu ===")
        print("1. Unequip Weapon")
        print("2. Unequip Armour")
        print("3. Unequip All")
        print("0. Back")

        choice = input("Choose: ")

        if choice == "1":
            if equipped_weapon:
                print(f"{equipped_weapon['name']} unequipped.")
                equipped_weapon = None
            else:
                print("No weapon equipped.")

        elif choice == "2":
            if equipped_armour:
                print(f"{equipped_armour['name']} unequipped.")
                equipped_armour = None
            else:
                print("No armour equipped.")

        elif choice == "3":
            equipped_weapon = None
            equipped_armour = None
            print("All equipment removed.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")
            
def sell_item():
    global gold, equipped_weapon, equipped_armour

    if len(inventory) == 0:
        print("Inventory is empty. Nothing to sell.")
        return

    show_inventory()
    choice = input("Choose item number to sell (0 to cancel): ")

    if choice == "0":
        return

    if not choice.isdigit():
        print("Invalid input!")
        return

    choice = int(choice)

    if choice < 1 or choice > len(inventory):
        print("Invalid item number.")
        return

    item = inventory[choice - 1]

    # Prevent selling equipped items
    if equipped_weapon is not None and item == equipped_weapon:
        print("You cannot sell an equipped weapon. Unequip it first.")
        return

    if equipped_armour is not None and item == equipped_armour:
        print("You cannot sell equipped armour. Unequip it first.")
        return

    sell_price = item["price"] // 2
    gold += sell_price

    sold_item = inventory.pop(choice - 1)

    print(f"You sold {sold_item['name']} for {sell_price} gold!")
    print("Gold:", gold)