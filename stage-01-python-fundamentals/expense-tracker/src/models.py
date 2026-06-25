from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Expense:
    amount: float
    category: str
    note: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "note": self.note,
            "created_at": self.created_at
        }