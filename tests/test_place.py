# tests/test_place.py
import unittest
import uuid
from models.place import Place
from models.amenity import Amenity

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place(name="Test Place", description="A nice place", price=100, location="123 Street", city_id=uuid.uuid4(), host_id=uuid.uuid4())
        self.amenity = Amenity(name="WiFi")

    def test_add_amenity(self):
        self.place.add_amenity(self.amenity)
        self.assertEqual(len(self.place.amenities), 1)
        self.assertEqual(self.place.amenities[0].name, "WiFi")

    def test_add_duplicate_amenity(self):
        self.place.add_amenity(self.amenity)
        with self.assertRaises(ValueError):
            self.place.add_amenity(self.amenity)

if __name__ == '__main__':
    unittest.main()
