import uuid
from datetime import datetime

class City:
    def __init__(self, name, country_id):
        self.city_id = uuid.uuid4()
        self.name = name
        self.country_id = country_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []

    def add_place(self, place):
        self.places.append(place)
        return place
