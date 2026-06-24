from dataclasses import dataclass
from datetime import datetime


@dataclass
class Expense:
    amount: float
    category: str
    note: str
    created_at: str = datetime.now().isoformat()

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "note": self.note,
            "created_at": self.created_at
        }