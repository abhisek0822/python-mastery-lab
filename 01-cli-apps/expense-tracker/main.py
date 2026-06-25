import argparse
from dbm import error
from src.services import add_expense, get_all_expenses, get_category_summary, get_monthly_summary

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

    else:
        parser.print_help()


if __name__ == "__main__":
    main()