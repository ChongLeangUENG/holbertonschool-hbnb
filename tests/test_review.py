# tests/test_review.py
import unittest
import uuid
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.user_id = uuid.uuid4()
        self.place_id = uuid.uuid4()
        self.review = Review(user_id=self.user_id, place_id=self.place_id, rating=5, comment="Great place!")

    def test_review_creation(self):
        self.assertEqual(self.review.user_id, self.user_id)
        self.assertEqual(self.review.place_id, self.place_id)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Great place!")

if __name__ == '__main__':
    unittest.main()
