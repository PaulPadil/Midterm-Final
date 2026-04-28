import json

       
# =========================
# DEFAULT PLAYER DATA
# =========================
gold = 1000
base_attack = 10
base_defense = 5

equipped_weapon = None
equipped_armour = None
inventory = []


# =========================
# FUNCTION: SAVE GAME
# =========================
def save_game():
    data = {
        "gold": gold,
        "inventory": inventory,
        "equipped_weapon": equipped_weapon,
        "equipped_armour": equipped_armour
    }

    with open("save_data.json", "w") as file:
        json.dump(data, file)


# =========================
# FUNCTION: LOAD GAME
# =========================
def load_game():
    global gold, inventory, equipped_weapon, equipped_armour

    try:
        with open("save_data.json", "r") as file:
            data = json.load(file)
            gold = data["gold"]
            inventory = data["inventory"]
            equipped_weapon = data["equipped_weapon"]
            equipped_armour = data["equipped_armour"]
    except FileNotFoundError:
        print("No save file found. Starting new game.")


# =========================
# FUNCTION: SAVE ITEM TO INVENTORY
# Now includes PRICE for selling later
# =========================
def save_item(item_type, item_name, power, price):
    inventory.append({
        "type": item_type,
        "name": item_name,
        "power": power,
        "price": price
    })
    save_game()


# =========================
# FUNCTION: SHOW INVENTORY
# =========================
def show_inventory():
    print("\n=== Inventory ===")

    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for i in range(len(inventory)):
            item = inventory[i]

            if item["type"] == "Weapon":
                print(f"{i + 1}. {item['name']} (Weapon, ATK +{item['power']}, Price {item['price']})")

            elif item["type"] == "Armour":
                print(f"{i + 1}. {item['name']} (Armour, DEF +{item['power']}, Price {item['price']})")


# =========================
# FUNCTION: EQUIP / USE ITEM
# =========================
def use_item():
    global equipped_weapon, equipped_armour

    if len(inventory) == 0:
        print("\033[31m\nInventory is empty. Nothing to equip.\033[0m")
        return

    show_inventory()
    choice = input("\033[33mChoose item number to equip (0 to cancel):\033[0m ")

    if choice == "0":
        return

    if not choice.isdigit():
        print("\033[31mInvalid input! Please enter a number.\033[0m")
        return

    choice = int(choice)

    if choice < 1 or choice > len(inventory):
        print("\033[31mInvalid item number.\033[0m")
        return

    item = inventory[choice - 1]

    if item["type"] == "Weapon":
        equipped_weapon = item
        print(f"\033[33mYou equipped\033[0m {item['name']}!\033[31m ATK \033[0m +{item['power']}")

    elif item["type"] == "Armour":
        equipped_armour = item
        print(f"\033[33mYou equipped\033[0m {item['name']}!\033[34m DEF\033[0m +{item['power']}")

    save_game()


# =========================
# FUNCTION: UNEQUIP ITEM
# =========================
def unequip_item():
    global equipped_weapon, equipped_armour
 
    while True:
        print("\n\033[33m=== Unequip Menu ===\033[0m")
        print("\033[32m1. Unequip Weapon\033[0m")
        print("\033[32m2. Unequip Armour\033[0m")
        print("\033[32m3. Unequip All\033[0m")
        print("\033[32m0. Back\033[0m")

        choice = input("\033[32mChoose option: \033[0m")

        if choice not in ["1", "2", "3", "0"]:
            print("\033[31mInvalid choice! Please choose 0 to 3 only.\033[0m")
            continue

        if choice == "1":
            if equipped_weapon is None:
                print("\033[32mNo weapon is equipped.\033[0m")
            else:
                print(f"\033[32m{equipped_weapon['name']} has been unequipped.\033[0m")
                equipped_weapon = None
                save_game()

        elif choice == "2":
            if equipped_armour is None:
                print("\033[32mNo armour is equipped.\033[0m")
            else:
                print(f"\033[32m{equipped_armour['name']} has been unequipped.\033[0m")
                equipped_armour = None
                save_game()

        elif choice == "3":
            if equipped_weapon is None and equipped_armour is None:
                print("\033[32mNothing is equipped.\033[0m")
            else:
                equipped_weapon = None
                equipped_armour = None
                print("\033[32mAll equipment has been unequipped.\033[0m")
                save_game()

        elif choice == "0":
            break


# =========================
# FUNCTION: SELL ITEM
# Sell price = half of original price
# =========================
def sell_item():
    global gold, equipped_weapon, equipped_armour

    if len(inventory) == 0:
        print("\033[31mInventory is empty. Nothing to sell.\033[0m\n")
        return

    show_inventory()
    choice = input("\033[33mChoose item number to sell (0 to cancel): \033[0m")

    if choice == "0":
        return

    if not choice.isdigit():
        print("\033[31mInvalid input! Please enter a number.\033[0m\n")
        return

    choice = int(choice)

    if choice < 1 or choice > len(inventory):
        print("\033[31mInvalid item number.\033[0m\n")
        return

    item = inventory[choice - 1]

    # Prevent selling equipped item unless unequipped first
    if equipped_weapon is not None and item == equipped_weapon:
        print("\033[31mYou cannot sell an equipped weapon. Unequip it first.\033[0m")
        return

    if equipped_armour is not None and item == equipped_armour:
        print("\033[31mYou cannot sell equipped armour. Unequip it first.\033[0m")
        return

    sell_price = item["price"] // 2
    gold += sell_price

    sold_item = inventory.pop(choice - 1)

    print(f"\033[33mYou sold {sold_item['name']} for {sell_price} gold!\033[0m")
    print("\033[33mYour Gold:\033[0m", gold)

    save_game()


# =========================
# FUNCTION: SHOW STATS
# =========================
def show_stats():
    weapon_attack = 0
    armour_defense = 0

    if equipped_weapon is not None:
        weapon_attack = equipped_weapon["power"]

    if equipped_armour is not None:
        armour_defense = equipped_armour["power"]

    total_attack = base_attack + weapon_attack
    total_defense = base_defense + armour_defense

    print("\n=== Player Stats ===")
    print("\033[33mGold:\033[0m", gold)
    print("\033[32mBase Attack\033[0m:", base_attack)
    print("\033[32mBase Defense:\033[0m", base_defense)

    if equipped_weapon is not None:
        print(f"\033[32mEquipped Weapon:\033[0m {equipped_weapon['name']} (ATK +{equipped_weapon['power']})")
    else:
        print("\033[31mEquipped Weapon: None\033[0m")

    if equipped_armour is not None:
        print(f"\033[32mEquipped Armour:\033[0m {equipped_armour['name']} (DEF +{equipped_armour['power']})")
    else:
        print("\033[32mEquipped Armour: None\033[0m")

    print("\033[31mTotal Attack:\033[0m", total_attack)
    print("\033[34mTotal Defense:\033[0m", total_defense)


# =========================
# FUNCTION: WEAPON SHOP
# =========================
def weapon_shop():
    global gold

    weapon_names = ["\033[32mOl’ Reliable\033[0m", "\033[32mDwarve’s Pride\033[0m", "\033[32mBandit King\033[0m",
                    "\033[32mWarrior’s Spirit\033[0m", "\033[32mLord’s Edge\033[0m", "\033[32mDragon Slayer\033[0m", 
                    "\033[32mHell Crusher\033[0m", "\033[32mHeaven Piercer\033[0m"]

    weapon_prices = [100, 500, 750, 1250, 2000, 2750, 3250, 4500]
    weapon_attacks = [15, 25, 45, 90, 100, 145, 200, 250]

    while True:
        print("\n\033[33m=== Weapon Shop ===\033[0m")
        print("\033[33mYour Gold:\033[0m", gold)

        for i in range(len(weapon_names)):
            print(f"{i + 1}. {weapon_names[i]} - \033[033mGold \033[0m {weapon_prices[i]} - \033[031mATK \033[0m+{weapon_attacks[i]}")

        print("0. Back")
        choice = input("\033[32mChoose weapon: \033[0m")

        if choice == "0":
            break

        if not choice.isdigit():
            print("\033[31mInvalid input! Please enter a number.\033[0m")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(weapon_names):
            print("\033[31mInvalid weapon choice.\033[0m")
            continue

        index = choice - 1
        chosen_weapon = weapon_names[index]
        price = weapon_prices[index]
        attack = weapon_attacks[index]

        if gold >= price:
            gold -= price
            save_item("Weapon", chosen_weapon, attack, price)
            print(f"\033[32m{chosen_weapon} bought successfully!\033[0m")
            print(f"\033[32mIt was added to your inventory. ATK +{attack}\033[0m")
            print("\033[33mGold left:\033[0m", gold)
            save_game()
        else:
            print("\033[31mNot enough gold!\033[0m")


# =========================
# FUNCTION: ARMOUR SHOP
# =========================
def armour_shop():
    global gold

    armour_names = ["\033[32mAdventurer’s Beginner Armor\033[0m", "\033[32mMyhtril Armor\033[0m", "\033[32mBandit King’s Armor\033[0m", 
                    "\033[32mWarrior\033[0m", "\033[32mLord’s Garments\033[0m", "\033[32mDragon King\033[0m", "\033[32mHell’s Tainted\033[0m", 
                    "\033[32mHeaven’s Blessed\033[0m"]
    armour_prices = [100, 750, 1000, 1500, 2250, 3000, 3500, 5000]
    armour_defenses = [50, 100, 125, 175, 200, 250, 375, 425]

    while True:
        print("\033[33m\n=== Armour Shop ===\033[0m")
        print("\033[33mYour Gold:\033[0m", gold,"\n")

        for i in range(len(armour_names)):
            print(f"{i + 1}. {armour_names[i]} - \033[033mGold \033[0m{armour_prices[i]}  - \033[034mDEF \033[0m+{armour_defenses[i]}")

        print("\033[31m0. Back\033[0m\n")
        choice = input("\033[33mChoose armour: \033[0m")

        if choice == "0":
            break

        if not choice.isdigit():
            print("\033[31mInvalid input! Please enter a number.\033[0m")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(armour_names):
            print("\033[31mInvalid armour choice.\033[0m")
            continue

        index = choice - 1
        chosen_armour = armour_names[index]
        price = armour_prices[index]
        defense = armour_defenses[index]

        if gold >= price:
            gold -= price
            save_item("\033[33mArmour\033[0m", chosen_armour, defense, price)
            print(f"{chosen_armour} \033[33mbought successfully!\033[0m")
            print(f"\033[32mIt was added to your inventory.\033[0m \033[34mDEF +{defense}\033[0m")
            print("\033[33mGold left: \033[0m", gold)
            save_game()
        else:
            print("\033[31mNot enough gold!\033[0m")


# =========================
# FUNCTION: MAIN MENU
# =========================
def main_menu():
    while True:
        
        #COLOR POLLLLLLLLLLLLL
        #30-Black
        #31-red
        #32-green
        #33-Yellow
        #34-blue
        #35-Purple
        #36-Cyan

        #COLOR BG POLLLLLLLLLLLLL
        #41-BG RED White text
        #32-BG green White text
        #33-BG Yellow White text
        #34-BG blue White text
        #35-BG Purple White text
        #36-BG Cyan White text

        print("\033[33m=== MAIN SHOP MENU ===\033[0m\n")
        print("\033[32m1. Weapon Shop\033[0m")
        print("\033[32m2. Armour Shop\033[0m")
        print("\033[32m3. Inventory\033[0m")
        print("\033[32m4. Equip / Use Item\033[0m")
        print("\033[32m5. Unequip Item\033[0m")
        print("\033[32m6. Sell Item\033[0m")
        print("\033[32m7. Stats\033[0m")
        print("\033[31m8. Exit\033[0m\n")

        choice = input("\033[33mSelect option: \033[0m")

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("\033[31mInvalid option! Please choose 1 to 8 only.\033[0m")
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
            print("\033[33mGame saved. Goodbye!\033[0m")
            save_game()
            break


# =========================
# START PROGRAM
# =========================
load_game()
main_menu()
# TESTING