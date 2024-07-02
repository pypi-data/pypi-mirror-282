"""This is a sample CLI program."""

from argparse import ArgumentParser


def main(s: str = "hello cli") -> None:
    """
    This is the main function, print `s` on screen

    Args:
        s: The string to print
    Returns:
        None
    """
    print(s)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-s", "--string", help="The string to print", type=str, required=True
    )
    args = parser.parse_args()
    main(args.string)
