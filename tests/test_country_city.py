import unittest
import uuid
from models.country import Country
from models.city import City
from models.place import Place

class TestCountryCity(unittest.TestCase):
    def setUp(self):
        self.country = Country(name="Wonderland")
        self.city = City(name="Dream City", country_id=self.country.country_id)

    def test_add_city_to_country(self):
        self.country.add_city(self.city)
        self.assertEqual(len(self.country.cities), 1)
        self.assertEqual(self.country.cities[0].name, "Dream City")

    def test_add_place_to_city(self):
        place = Place(name="Test Place", description="A nice place", price=100, location="123 Street", city_id=self.city.city_id, host_id=uuid.uuid4())
        self.city.add_place(place)
        self.assertEqual(len(self.city.places), 1)
        self.assertEqual(self.city.places[0].name, "Test Place")

if __name__ == '__main__':
    unittest.main()
