import unittest
from app import app

class UserApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        response = self.app.post('/users/', json={
            'email': 'jane.doe@example.com',
            'first_name': 'Jane',
            'last_name': 'Doe'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('user_id', data)
        self.assertEqual(data['email'], 'jane.doe@example.com')

    def test_get_user(self):
        response = self.app.post('/users/', json={
            'email': 'john.doe@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        })
        self.assertEqual(response.status_code, 201)
        user_id = response.get_json()['user_id']

        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['email'], 'john.doe@example.com')

    def test_update_user(self):
        response = self.app.post('/users/', json={
            'email': 'john.smith@example.com',
            'first_name': 'John',
            'last_name': 'Smith'
        })
        self.assertEqual(response.status_code, 201)
        user_id = response.get_json()['user_id']

        response = self.app.put(f'/users/{user_id}', json={
            'first_name': 'Johnny'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['first_name'], 'Johnny')

    def test_delete_user(self):
        response = self.app.post('/users/', json={
            'email': 'doe.john@example.com',
            'first_name': 'Doe',
            'last_name': 'John'
        })
        self.assertEqual(response.status_code, 201)
        user_id = response.get_json()['user_id']

        response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204)

        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
