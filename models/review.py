import uuid
from datetime import datetime

class Review:
    def __init__(self, user_id, place_id, rating, comment):
        self.review_id = uuid.uuid4()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
