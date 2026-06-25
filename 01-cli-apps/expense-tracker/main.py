import argparse
from dbm import error
from src.services import add_expense, get_all_expenses


def main():
    parser = argparse.ArgumentParser(description="CLI Expense Tracker")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--category", type=str, required=True)
    add_parser.add_argument("--note", type=str, required=True)

    subparsers.add_parser("list", help="List all expenses")

    args = parser.parse_args()

    if args.command == "add":
        try:
            add_expense(args.amount, args.category, args.note)
            print("Expense added successfully.")
        except ValueError as error:
            print(f"Error: {error}")

    elif args.command == "list":
        expenses = get_all_expenses()

        for expense in expenses:
            print(
                f"{expense['created_at']} | "
                f"{expense['category']} | "
                f"{expense['amount']} | "
                f"{expense['note']}"
            )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()