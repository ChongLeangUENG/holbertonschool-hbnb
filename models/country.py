import uuid
from datetime import datetime

class Country:
    def __init__(self, name):
        self.country_id = uuid.uuid4()
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)
        return city
