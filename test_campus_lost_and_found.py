"""Checks that campus_lost_and_found.py correctly manages campus items."""

import unittest
from campus_lost_and_found import CampusLostAndFound


class CampusLostAndFoundTests(unittest.TestCase):
    def setUp(self):
        self.service = CampusLostAndFound()

    # Test Case 1: Reporting a lost item
    def test_report_lost_item(self):
        item = self.service.report_lost(
            title="Blue Water Bottle",
            category="Bottles",
            location="Library 2nd Floor",
            description="Milton stainless steel bottle",
        )
        self.assertEqual(item.id, 1)
        self.assertEqual(item.title, "Blue Water Bottle")
        self.assertEqual(item.status, "lost")

    # Test Case 2: Reporting a found item
    def test_report_found_item(self):
        item = self.service.report_found(
            title="Scientific Calculator",
            category="Electronics",
            location="Room 304",
            description="Casio fx-991EX left on desk",
        )
        self.assertEqual(item.id, 1)
        self.assertEqual(item.title, "Scientific Calculator")
        self.assertEqual(item.status, "found")

    # Test Case 3: Finding items by keyword search
    def test_find_items_by_keyword(self):
        self.service.report_lost("Blue Backpack", "Bags", "Cafeteria", "Contains notebooks")
        self.service.report_found("Black Wallet", "Accessories", "Sports Complex", "Found near gym")

        results = self.service.find_items(keyword="backpack")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Blue Backpack")

    # Test Case 4: Claiming an item
    def test_claim_item(self):
        item = self.service.report_found("Keys with Red Lanyard", "Keys", "Main Gate")
        claimed_item = self.service.claim_item(item.id)
        self.assertEqual(claimed_item.status, "claimed")




if __name__ == "__main__":
    unittest.main()
