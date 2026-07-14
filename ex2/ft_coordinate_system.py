import math


def get_player_pos() -> tuple[float, float, float]:
    user_input = input(
        "Enter new coordinates as floats in format 'x,y,z': ")
    parts = user_input.split(",")
    length = 0
    for _ in parts:
        length += 1
    if length != 3:
        print("Invalid syntax")
        return get_player_pos()
    try:
        for part in parts:
            float(part)
    except ValueError as e:
        print(f"Error on parameter '{part}': {e}")
        return get_player_pos()

    return (float(parts[0]),
            float(parts[1]),
            float(parts[2])
            )


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    first_player = get_player_pos()
    print(f"Got a first tuple: {first_player}")
    x1 = first_player[0]
    y1 = first_player[1]
    z1 = first_player[2]
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance = x1**2 + y1**2 + z1**2
    distance = round(math.sqrt(distance), 4)
    print(f"Distance to center: {distance}")

    print("\nGet a second set of coordinates")
    second_player = get_player_pos()
    x2 = second_player[0]
    y2 = second_player[1]
    z2 = second_player[2]
    distance = (x2 - x1)**2 + (y2-y1)**2 + (z2-z1)**2
    distance = round(math.sqrt(distance), 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    main()
