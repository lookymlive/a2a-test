import sys


def main() -> None:
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "a2a-test"
    print(f"Hello from {name}!")


if __name__ == "__main__":
    main()
