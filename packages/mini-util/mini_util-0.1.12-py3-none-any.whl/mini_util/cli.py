"""This is a sample CLI program."""

from argparse import ArgumentParser


def main() -> None:
    """
    This is the main function, print `s` on screen

    Args:
        s: The string to print
    Returns:
        None
    """
    parser = ArgumentParser()
    parser.add_argument(
        "-s", "--string", help="The string to print", type=str, required=True
    )
    args = parser.parse_args()
    print(args.string)


if __name__ == "__main__":
    main()
