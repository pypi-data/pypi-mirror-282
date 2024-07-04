import argparse
from toolsworks.core import greet
from toolsworks.helper import add

def main():
    parser = argparse.ArgumentParser(description="Toolsworks CLI")
    subparsers = parser.add_subparsers(dest="command")

    greet_parser = subparsers.add_parser("greet", help="Greet someone")
    greet_parser.add_argument("name", type=str, help="Name to greet")

    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=int, help="First number")
    add_parser.add_argument("b", type=int, help="Second number")

    args = parser.parse_args()

    if args.command == "greet":
        print(greet(args.name))
    elif args.command == "add":
        print(add(args.a, args.b))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

