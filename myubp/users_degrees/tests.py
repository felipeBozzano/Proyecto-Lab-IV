from django.test import TestCase, Client
import json

from users.models import UserProfile


class UserDegreeTest(TestCase):

    def setUp(self):
        self.browser = Client()

        ''' ROOT WORK '''
        """ Create a root user just needed for create a degree """
        self.test_root = UserProfile.objects.create(email='root@root.root',
                                                    name='root',
                                                    is_active=True,
                                                    is_staff=True,
                                                    is_superuser=True)
        self.test_root.set_password('root')
        self.test_root.save()

        ''' Login with new root user '''
        login = self.browser.post('/api/login/', {'username': 'root@root.root', 'password': 'root'})
        token = "Token " + json.loads(login.content)['token']
        self.browser.defaults['HTTP_AUTHORIZATION'] = token

        """Create a new degree using the degree API"""
        self.new_degree_1 = self.browser.post('/api/degrees/', {'name': 'TestDegree1',
                                                                'approval_note': 4}, HTTP_AUTHORIZATION=token)

        """Create a new degree using the degree API"""
        self.new_degree_2 = self.browser.post('/api/degrees/', {'name': 'TestDegree2',
                                                                'approval_note': 4}, HTTP_AUTHORIZATION=token)

        ''' TEST USER (NOT ROOT) WORK '''
        """ Create a new test user """
        self.test_user = UserProfile.objects.create(email='test@test.test',
                                                    name='test user',
                                                    is_active=True,
                                                    is_staff=False)
        self.test_user.set_password('test1234')
        self.test_user.save()

        ''' Login with new test user '''
        login = self.browser.post('/api/login/', {'username': 'test@test.test', 'password': 'test1234'})
        self.token = "Token " + json.loads(login.content)['token']
        self.browser.defaults['HTTP_AUTHORIZATION'] = self.token

    def test_update_exam_note(self):
        """Create a new UserDegree"""
        self.browser.post('/api/users_degrees/', {'id_user': 2,
                                                  'id_degree': 1})

        user_degree = self.browser.get('/api/users_degrees/', content_type="application/json")

        # Convert string to List
        list_user_degree = user_degree.json()

        # Convert List to dict
        degree_id = list_user_degree[0].get('id_degree')
        user_id = list_user_degree[0].get('id_user')

        # Check the assert
        self.assertEqual(degree_id, 1)
        self.assertEqual(user_id, 2)


