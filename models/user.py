import uuid
from datetime import datetime
from models.place import Place
from models.review import Review

class User:
    def __init__(self, email, first_name, last_name, password):
        self.user_id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []

    def create_place(self, name, description, price, location, city_id):
        place = Place(name, description, price, location, city_id, self.user_id)
        self.places.append(place)
        return place

    def add_review(self, place, rating, comment):
        review = Review(self.user_id, place.place_id, rating, comment)
        place.reviews.append(review)
        return review
