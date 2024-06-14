import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name):
        self.amenity_id = uuid.uuid4()
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
