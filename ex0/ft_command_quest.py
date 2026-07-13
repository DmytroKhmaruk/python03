import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 0
        for arg in sys.argv[1:]:
            i += 1
            print(f"Argument {i}: {arg}")

    print(f"Total arguments: {len(sys.argv)}\n")
