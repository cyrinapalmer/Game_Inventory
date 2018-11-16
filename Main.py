inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        total += v
    print("Total number of items: " + str(total))

display_inventory(inventory)

def add_to_inventory(inventory, added_items):
    for each in added_items:
        if each in inventory:
            inventory[each] += 1
        else:
            inventory[each] = 1

add_to_inventory(inventory, dragonLoot)
display_inventory(inventory)
