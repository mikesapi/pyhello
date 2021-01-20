"""Simple Hello World Python script."""

import argparse
import logging
import sys


def main() -> None:
    """Simple Hello World Python script."""
    parser = argparse.ArgumentParser(description='Simple Hello World Python script.')
    parser.add_argument("--magic_number", "-m", default=42, help="A magic number.")
    args = parser.parse_args()

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logging.info(f"Hello World {args.magic_number}")


if __name__ == "__main__":
    main()
