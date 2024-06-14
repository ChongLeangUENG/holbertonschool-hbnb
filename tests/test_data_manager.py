import unittest
import uuid
from models.user import User
from models.place import Place
from persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.user = User(email="test@example.com", first_name="Test", last_name="User", password="password123")
        self.place = Place(name="Test Place", description="A nice place", price=100, location="123 Street", city_id=uuid.uuid4(), host_id=self.user.user_id)

    def test_save_and_get_user(self):
        self.data_manager.save(self.user)
        retrieved_user = self.data_manager.get(self.user.user_id, User)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, "test@example.com")

    def test_update_user(self):
        self.data_manager.save(self.user)
        self.user.first_name = "Updated"
        self.data_manager.update(self.user)
        updated_user = self.data_manager.get(self.user.user_id, User)
        self.assertEqual(updated_user.first_name, "Updated")

    def test_delete_user(self):
        self.data_manager.save(self.user)
        self.data_manager.delete(self.user.user_id, User)
        deleted_user = self.data_manager.get(self.user.user_id, User)
        self.assertIsNone(deleted_user)

    def test_save_and_get_place(self):
        self.data_manager.save(self.place)
        retrieved_place = self.data_manager.get(self.place.place_id, Place)
        self.assertIsNotNone(retrieved_place)
        self.assertEqual(retrieved_place.name, "Test Place")

if __name__ == '__main__':
    unittest.main()
