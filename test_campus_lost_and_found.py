"""Checks that campus_lost_and_found.py correctly manages campus items."""

import unittest
from campus_lost_and_found import CampusLostAndFound


class CampusLostAndFoundTests(unittest.TestCase):
    def setUp(self):
        self.service = CampusLostAndFound()

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

    def test_report_found_item(self):
        item = self.service.report_found(
            title="Scientific Calculator",
            category="Electronics",
            location="Room 304",
            description="Casio fx-991EX left on desk",
        )
        self.assertEqual(item.id, 1)
        self.assertEqual(item.status, "found")

    def test_empty_title_raises_error(self):
        with self.assertRaises(ValueError):
            self.service.report_lost("", "Electronics", "Library")

    def test_empty_location_raises_error(self):
        with self.assertRaises(ValueError):
            self.service.report_found("ID Card", "ID Cards", "")

    def test_find_items_by_keyword(self):
        self.service.report_lost("Blue Backpack", "Bags", "Cafeteria", "Contains notebooks")
        self.service.report_found("Black Wallet", "Accessories", "Sports Complex", "Found near gym")

        results = self.service.find_items(keyword="backpack")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Blue Backpack")

    def test_find_items_by_category_and_status(self):
        self.service.report_lost("Calculus Notebook", "Books", "Library")
        self.service.report_found("Physics Textbook", "Books", "Lab 2")
        self.service.report_found("USB Drive", "Electronics", "Lab 1")

        found_books = self.service.find_items(category="Books", status="found")
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].title, "Physics Textbook")

    def test_claim_item(self):
        item = self.service.report_found("Keys with Red Lanyard", "Keys", "Main Gate")
        claimed_item = self.service.claim_item(item.id)
        self.assertEqual(claimed_item.status, "claimed")

    def test_claim_already_claimed_raises_error(self):
        item = self.service.report_found("Earphones", "Electronics", "Hostel Block A")
        self.service.claim_item(item.id)
        with self.assertRaises(ValueError):
            self.service.claim_item(item.id)

    def test_claim_non_existent_item_raises_error(self):
        with self.assertRaises(KeyError):
            self.service.claim_item(999)


if __name__ == "__main__":
    unittest.main()
