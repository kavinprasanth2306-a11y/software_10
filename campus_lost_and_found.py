"""Campus Lost and Found system for tracking and finding lost items."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Item:
    id: int
    title: str
    category: str
    location: str
    description: str
    status: str = "lost"  # "lost", "found", "claimed"
    date_reported: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))


class CampusLostAndFound:
    def __init__(self):
        self._items: List[Item] = []
        self._next_id: int = 1

    def report_lost(self, title: str, category: str, location: str, description: str = "") -> Item:
        """Report an item that was lost on campus."""
        if not title.strip():
            raise ValueError("Item title cannot be empty")
        if not location.strip():
            raise ValueError("Location cannot be empty")

        item = Item(
            id=self._next_id,
            title=title.strip(),
            category=category.strip(),
            location=location.strip(),
            description=description.strip(),
            status="lost",
        )
        self._items.append(item)
        self._next_id += 1
        return item

    def report_found(self, title: str, category: str, location: str, description: str = "") -> Item:
        """Report an item that was found on campus."""
        if not title.strip():
            raise ValueError("Item title cannot be empty")
        if not location.strip():
            raise ValueError("Location cannot be empty")

        item = Item(
            id=self._next_id,
            title=title.strip(),
            category=category.strip(),
            location=location.strip(),
            description=description.strip(),
            status="found",
        )
        self._items.append(item)
        self._next_id += 1
        return item

    def find_items(
        self,
        keyword: Optional[str] = None,
        category: Optional[str] = None,
        location: Optional[str] = None,
        status: Optional[str] = None,
    ) -> List[Item]:
        """Search and filter items in campus lost & found."""
        results = self._items

        if keyword:
            kw = keyword.lower()
            results = [
                item
                for item in results
                if kw in item.title.lower() or kw in item.description.lower()
            ]

        if category:
            results = [item for item in results if item.category.lower() == category.lower()]

        if location:
            results = [item for item in results if location.lower() in item.location.lower()]

        if status:
            results = [item for item in results if item.status.lower() == status.lower()]

        return results

    def claim_item(self, item_id: int) -> Item:
        """Mark a found or lost item as claimed by its rightful owner."""
        for item in self._items:
            if item.id == item_id:
                if item.status == "claimed":
                    raise ValueError(f"Item with id {item_id} is already claimed")
                item.status = "claimed"
                return item
        raise KeyError(f"Item with id {item_id} not found")

    def get_item(self, item_id: int) -> Optional[Item]:
        """Retrieve an item by its unique ID."""
        for item in self._items:
            if item.id == item_id:
                return item
        return None
