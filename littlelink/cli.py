import argparse
import generate


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--create-config",
        action='store_true',
        default=False,
        help="Creates an empty config file to add services and links.",
    )

    parser.add_argument(
        "--generate",
        action='store_true',
        default=False,
        help="Generate link Page",
    )

    options = parser.parse_args()
    generate.main(vars(options))


if __name__ == '__main__':
    main()

