import argparse
from dbm import error
from src.services import (
    add_expense,
    get_all_expenses,
    get_category_summary,
    get_monthly_summary,
    export_expenses_to_csv
)

def main():
    parser = argparse.ArgumentParser(description="CLI Expense Tracker")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--category", type=str, required=True)
    add_parser.add_argument("--note", type=str, required=True)

    subparsers.add_parser("list", help="List all expenses")
    
    subparsers.add_parser("summary", help="Show category-wise expense summary")
    
    monthly_parser = subparsers.add_parser("monthly", help="Show monthly expense summary")
    monthly_parser.add_argument("--year", type=int, required=True)
    monthly_parser.add_argument("--month", type=int, required=True)

    export_parser = subparsers.add_parser("export", help="Export expenses to CSV")
    export_parser.add_argument("--file", type=str, default="expenses_export.csv")

    args = parser.parse_args()

    if args.command == "add":
        try:
            add_expense(args.amount, args.category, args.note)
            print("Expense added successfully.")
        except ValueError as error:
            print(f"Error: {error}")

    elif args.command == "list":
        expenses = get_all_expenses()

        if not expenses:
            print("No expenses found.")
        else:
            print("-" * 75)
            print(f"{'Date':<20} {'Category':<15} {'Amount':<10} {'Note':<25}")
            print("-" * 75)

            for expense in expenses:
                date = expense["created_at"][:10]
                category = expense["category"]
                amount = expense["amount"]
                note = expense["note"]

                print(f"{date:<20} {category:<15} {amount:<10} {note:<25}")

            print("-" * 75)

    elif args.command == "summary":
        summary = get_category_summary()

        if not summary:
            print("No expenses found.")
        else:
            for category, total in summary.items():
                print(f"{category}: {total}")

    elif args.command == "monthly":
        result = get_monthly_summary(args.year, args.month)

        if not result["summary"]:
            print("No expenses found for this month.")
        else:
            print(f"Monthly Summary: {args.month}/{args.year}")
            print("-" * 30)

            for category, total in result["summary"].items():
                print(f"{category}: {total}")

            print("-" * 30)
            print(f"Total: {result['total']}")

    elif args.command == "export":
        file_name = export_expenses_to_csv(args.file)

        if file_name is None:
            print("No expenses found to export.")
        else:
            print(f"Expenses exported successfully to {file_name}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()