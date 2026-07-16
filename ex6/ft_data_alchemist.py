import random


def main() -> None:
    names = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    upper_list = [name.capitalize() for name in names]
    lower_list = [name.lower() for name in names]

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {upper_list}")
    print(f"New list of capitalized names only: {lower_list}")
    scores = {name: random.randint(1, 1000) for name in upper_list}
    print(f"Score dict: {scores}")
    score_average = sum(scores[name] / len(scores) for name in scores)
    print(f"Score average is {round(score_average, 2)}")
    high_scores = {n: scores[n] for n in scores if scores[n] > score_average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
