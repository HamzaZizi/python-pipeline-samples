import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_status_code(self):
        # Test that the home page returns a 200 status code
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        # Test that the home page contains expected content
        response = self.app.get('/')
        self.assertIn(b'<!DOCTYPE html>', response.data)  # Assuming 'index.html' starts with <!DOCTYPE html>

    def test_nonexistent_route(self):
        # Test a nonexistent route
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
