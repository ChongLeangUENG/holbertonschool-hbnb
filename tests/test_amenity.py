# tests/test_amenity.py
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity(name="WiFi")

    def test_amenity_creation(self):
        self.assertEqual(self.amenity.name, "WiFi")

if __name__ == '__main__':
    unittest.main()
