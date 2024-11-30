# import unittest
# from app import app

# class FlaskAppTestCase(unittest.TestCase):
#     def setUp(self):
#         # Set up the test client
#         self.app = app.test_client()
#         self.app.testing = True

#     def test_home_page_status_code(self):
#         # Test that the home page returns a 200 status code
#         response = self.app.get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_home_page_content(self):
#         # Test that the home page contains expected content
#         response = self.app.get('/')
#         self.assertIn(b'<!DOCTYPE html>', response.data)  # Assuming 'index.html' starts with <!DOCTYPE html>

#     def test_nonexistent_route(self):
#         # Test a nonexistent route
#         response = self.app.get('/nonexistent')
#         self.assertEqual(response.status_code, 404)

# if __name__ == '__main__':
#     unittest.main()


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

    # New test for /generate_random endpoint
    def test_generate_random_status_code(self):
        # Test that the /generate_random route returns a 200 status code
        response = self.app.get('/generate_random')
        self.assertEqual(response.status_code, 200)

    def test_generate_random_json_response(self):
        # Test that the /generate_random route returns a valid JSON response
        response = self.app.get('/generate_random')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'random_number', response.data)  # Check that random_number is in the JSON response

    def test_generate_random_number_range(self):
        # Test that the random number generated is between 1 and 100
        response = self.app.get('/generate_random')
        data = response.json
        self.assertTrue(1 <= data['random_number'] <= 100)  # Ensure the random number is within the expected range

    def test_generate_random_content_type(self):
        # Test that the response content type is application/json for the /generate_random route
        response = self.app.get('/generate_random')
        self.assertEqual(response.content_type, 'application/json')

if __name__ == '__main__':
    unittest.main()
