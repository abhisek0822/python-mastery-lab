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