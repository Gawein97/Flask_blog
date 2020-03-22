from flaskblog import create_app
import unittest


app = create_app()


class FlaskRoutesTests(unittest.TestCase):


    def test_home(self):
        test = app.test_client(self)
        response = test.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
