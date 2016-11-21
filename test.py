from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    # Ensure that the flask set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(200, response.status_code)

    # Ensure that the login page loads correctly
    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Ensure that the login behaves correctly on correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'You are just logged in!', response.data)

    # Ensure that the login behaves correctly on incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="wrong", password="wrong"), follow_redirects=True)
        self.assertIn(b'Wrong admin!', response.data)

    # Ensure logout behaves correctly
    def test_logout_page(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You are just logged out!', response.data)

    # Ensure that the main page requires login
    def test_main_route_requires_loing(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'Please login' in response.data)

    #Ensure that the posts show up on main page
    def test_posts_show_up(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'I am good!', response.data)

if __name__ == '__main__':
    unittest.main()

