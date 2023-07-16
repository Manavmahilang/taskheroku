import unittest
from main import app

class FlaskAPITestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client for the Flask app
        self.app = app.test_client()
        # Set 'testing' to True, so that Flask doesn't catch exceptions and print them
        app.testing = True

    def test_get_all_bank_branches(self):
        response = self.app.get('/bank_branches')
        self.assertEqual(response.status_code, 200)
        # Assuming that the response will be a JSON array
        self.assertIsInstance(response.json, list)

    def test_get_branch_details_by_ifsc_code(self):
        ifsc_code = 'ABHY0065023'  # Replace with a valid IFSC code from the CSV file
        response = self.app.get(f'/bank_branches/{ifsc_code}')
        self.assertEqual(response.status_code, 200)
        # Assuming that the response will be a JSON object
        self.assertIsInstance(response.json, dict)

    def test_get_branch_by_name(self):
        branch_name = 'RAIPUR KHARKHARI  BIHAR'  # Replace with a valid branch name from the CSV file
        response = self.app.get(f'/bank_branches/branch/{branch_name}')
        self.assertEqual(response.status_code, 200)
        # Assuming that the response will be a JSON array
        self.assertIsInstance(response.json, list)

    def test_get_branch_by_city(self):
        city = 'TENALI'  # Replace with a valid city from the CSV file
        response = self.app.get(f'/bank_branches/city/{city}')
        self.assertEqual(response.status_code, 200)
        # Assuming that the response will be a JSON array
        self.assertIsInstance(response.json, list)

    def test_get_branch_by_district(self):
        district = 'RAIPUR'  # Replace with a valid district from the CSV file
        response = self.app.get(f'/bank_branches/district/{district}')
        self.assertEqual(response.status_code, 200)
        # Assuming that the response will be a JSON array
        self.assertIsInstance(response.json, list)

    def test_get_branch_by_state(self):
        state = 'GUJRAT'  # Replace with a valid state from the CSV file
        response = self.app.get(f'/bank_branches/state/{state}')
        self.assertEqual(response.status_code, 200)
        # Assuming that the response will be a JSON array
        self.assertIsInstance(response.json, list)

if __name__ == '__main__':
    unittest.main()
