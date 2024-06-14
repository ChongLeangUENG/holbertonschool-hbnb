import uuid
from datetime import datetime

class Place:
    def __init__(self, name, description, price, location, city_id, host_id):
        self.place_id = uuid.uuid4()
        self.name = name
        self.description = description
        self.price = price
        self.location = location
        self.city_id = city_id
        self.host_id = host_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            return amenity
        else:
            raise ValueError("Amenity already exists in this place")

    def add_review(self, review):
        self.reviews.append(review)
