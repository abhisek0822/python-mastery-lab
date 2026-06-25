import csv
from datetime import datetime
from src.models import Expense
from src.storage import save_expense, load_expenses


def add_expense(amount, category, note):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    if not category.strip():
        raise ValueError("Category cannot be empty")

    if not note.strip():
        raise ValueError("Note cannot be empty")

    expense = Expense(
        amount=amount,
        category=category.strip(),
        note=note.strip()
    )

    save_expense(expense)


def get_all_expenses():
    return load_expenses()

def get_category_summary():
    expenses = load_expenses()
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in summary:
            summary[category] = 0

        summary[category] += amount

    return summary

def get_monthly_summary(year, month):
    expenses = load_expenses()
    summary = {}
    total = 0

    for expense in expenses:
        expense_date = datetime.fromisoformat(expense["created_at"])

        if expense_date.year == year and expense_date.month == month:
            category = expense["category"]
            amount = expense["amount"]

            summary[category] = summary.get(category, 0) + amount
            total += amount

    return {
        "summary": summary,
        "total": total
    }

def export_expenses_to_csv(file_name="expenses_export.csv"):
    expenses = load_expenses()

    if not expenses:
        return None

    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["amount", "category", "note", "created_at"]
        )

        writer.writeheader()
        writer.writerows(expenses)

    return file_name