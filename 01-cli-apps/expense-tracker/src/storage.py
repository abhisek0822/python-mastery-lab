import json
from pathlib import Path


DATA_FILE = Path("expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_expense(expense):
    expenses = load_expenses()
    expenses.append(expense.to_dict())

    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)