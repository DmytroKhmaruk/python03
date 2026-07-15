import sys


def main() -> None:
    inventory = {}
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
        return

    for item in sys.argv[1:]:
        if len(item.split(":")) != 2:
            print(f"Error - invalid parameter '{item}'")
        else:
            key, value = item.split(":")
            try:
                if len(key) == 0:
                    print(f"Error - invalid parameter '{item}'")
                    continue
                if key in inventory:
                    print(f"Redundant item '{key}' - discarding")
                    continue
                value = int(value)

                inventory[key] = value
            except ValueError as e:
                print(f"Quantity error for '{key}': {e}")
    print(f"Got inventory: {inventory}")
    if len(inventory) == 0:
        print("Inventory is empty!")
        return

    print(f"Item list: {list(inventory.keys())}")
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    most_abundant = list(inventory.keys())[0]
    least_abundat = list(inventory.keys())[0]
    for item in inventory:
        value = inventory[item]
        value = value / total_quantity * 100
        print(f"Item {item} represents {round(value, 1)}%")
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundat]:
            least_abundat = item
    print(f"Item most abundant: {most_abundant} with quantity "
          f"{inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundat} with quantity "
          f"{inventory[least_abundat]}")
    key = "magic_item"
    value = 1
    inventory.update({key: value})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
