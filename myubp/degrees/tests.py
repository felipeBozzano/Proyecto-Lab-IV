from django.test import TestCase, Client
import json
from users.models import UserProfile


class PostDegreeCase(TestCase):

    def setUp(self):
        self.browser = Client()

        """Create a root user"""
        self.test_root = UserProfile.objects.create(email='root@root.root',
                                                    name='root',
                                                    is_active=True,
                                                    is_staff=True,
                                                    is_superuser=True)
        self.test_root.set_password('root')
        self.test_root.save()

        ''' Login with root user '''
        login = self.browser.post('/api/login/', {'username': 'root@root.root', 'password': 'root'})
        token = "Token " + json.loads(login.content)['token']
        self.browser.defaults['HTTP_AUTHORIZATION'] = token

        """Create a new degree using the degree API"""
        self.new_degree = self.browser.post('/api/degrees/', {'name': 'Degree',
                                                              'approval_note': 5}, HTTP_AUTHORIZATION=token)

        '''Convert byte object to string'''
        self.string_new_degree = self.new_degree.content.decode("utf-8").replace("'", '"')

        '''Convert string_new_degree to dict_new_degree'''
        self.dict_new_degree = json.loads(self.string_new_degree)
        self.new_degree_name = self.dict_new_degree.get('name')
        self.new_degree_approval_note = self.dict_new_degree.get('approval_note')

    def test_degree_data(self):
        """Verify correct degree data"""

        # Get all the degrees
        selected_degree = self.browser.get('/api/degrees/', content_type="application/json")

        # Convert byte_degree object to string_degree
        string_degree = selected_degree.content.decode("utf-8").replace("'", '"')

        # Convert string to dict
        dict_degree = json.loads(string_degree)[0]
        degree_name = dict_degree.get('name')
        degree_approval_note = dict_degree.get('approval_note')

        # Check the assert
        self.assertEqual(degree_name, self.new_degree_name)
        self.assertEqual(degree_approval_note, self.new_degree_approval_note)
