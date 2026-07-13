import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ...\n")
        return
    else:
        int_scorre_lst: list[int] = []
        for arg in sys.argv[1:]:
            try:
                int_scorre_lst.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: '{arg}'")

        if len(int_scorre_lst) == 0:
            print(
                "No scores provided. Usage: python3 ft_score_analytics.py "
                "<score1> <score2> ...\n")
            return

        total_players = len(int_scorre_lst)
        total_score = sum(int_scorre_lst)
        high_score = max(int_scorre_lst)
        low_score = min(int_scorre_lst)

        print(f"Scores processed: {int_scorre_lst}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {total_score / total_players}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {high_score - low_score}\n")


if __name__ == "__main__":
    main()
