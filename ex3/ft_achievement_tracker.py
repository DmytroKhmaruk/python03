import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    count = random.randint(1, len(achievements))
    player = set(random.sample(achievements, count))
    return player


def main() -> None:
    achievements = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'
    ]
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_ach = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_ach}")

    print(f"\nCommon achievements: {alice.intersection(bob, charlie, dylan)}")

    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")

    print(f"\nAlice is missing: {all_ach.difference(alice)}")
    print(f"Bob is missing: {all_ach.difference(bob)}")
    print(f"Charlie is missing: {all_ach.difference(charlie)}")
    print(f"Dylan is missing: {all_ach.difference(dylan)}")


if __name__ == "__main__":
    main()
