from django.test import TestCase, Client
import json

from users.models import UserProfile


class ProductTest(TestCase):

    def setUp(self):
        self.browser = Client()
        """Create a new test user using the profile API"""
        self.new_user = self.browser.post('/api/profile/', {'name': 'Usuario de Test',
                                                            'email': 'test_user@test.com',
                                                            'password': 'test123'})

        '''convert byte object to string'''
        self.string_new_user = self.new_user.content.decode("utf-8").replace("'", '"')
        '''convert string_new_user to dict_new_user'''
        self.dict_new_user = json.loads(self.string_new_user)
        self.new_user_name = self.dict_new_user.get('name')
        self.new_user_email = self.dict_new_user.get('email')

        ''' Login with new user '''
        login = self.browser.post('/api/login/', {'username': 'test_user@test.com', 'password': 'test123'})
        token = "Token " + json.loads(login.content)['token']
        self.browser.defaults['HTTP_AUTHORIZATION'] = token

    def test_user_data(self):
        """Verify correct user data"""
        loged_user = self.browser.get('/api/profile/', content_type="application/json")
        '''convert byte_loged_user object to string_user '''
        string_user = loged_user.content.decode("utf-8").replace("'", '"')
        '''convert string to dict'''
        dict_user = json.loads(string_user)[0]
        user_name = dict_user.get('name')
        user_email = dict_user.get('email')
        self.assertEqual(user_email, self.new_user_email)
        self.assertEqual(user_name, self.new_user_name)
