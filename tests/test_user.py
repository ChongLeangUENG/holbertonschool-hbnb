# tests/test_user.py
import unittest
import uuid
from models.user import User
from models.place import Place

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(email="test@example.com", first_name="John", last_name="Doe", password="password123")

    def test_create_place(self):
        place = self.user.create_place(name="Test Place", description="A nice place", price=100, location="123 Street", city_id=uuid.uuid4())
        self.assertEqual(len(self.user.places), 1)
        self.assertEqual(self.user.places[0].name, "Test Place")

    def test_add_review(self):
        place = self.user.create_place(name="Test Place", description="A nice place", price=100, location="123 Street", city_id=uuid.uuid4())
        review = self.user.add_review(place, rating=5, comment="Great place!")
        self.assertEqual(len(place.reviews), 1)
        self.assertEqual(place.reviews[0].rating, 5)
        self.assertEqual(place.reviews[0].comment, "Great place!")

if __name__ == '__main__':
    unittest.main()
