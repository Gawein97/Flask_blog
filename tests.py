from flaskblog import create_app
import unittest
from flaskblog.users.forms import RegistrationForm

app = create_app()


class FlaskRoutesTests(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('Set Up Main Routes Tests')
        cls.test = app.test_client(cls)


    def setUp(self):
        print('SetUp')

    def tearDown(self):
        print('tearDown\n')


    def test_home_route(self):
        print('test_home_route')
        response = self.test.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_home_route_2(self):
        print('test_home_route')
        response = self.test.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_about_route(self):
        print('test_about_route')
        response = self.test.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)


class FlaskPostsRoutesTests(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('Set Up Posts Routes Tests')
        cls.test = app.test_client(cls)


    def setUp(self):
        print('SetUp')


    def tearDown(self):
        print('tearDown\n')


    def test_new_post_route(self):
        print('test_new_post_route')
        response = self.test.get('/post/new', content_type='html/text')
        self.assertEqual(response.status_code, 302)



if __name__ == '__main__':
    unittest.main()
