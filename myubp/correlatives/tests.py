from django.test import TestCase, Client
import json

from users.models import UserProfile


class CorrelativesTest(TestCase):

    def setUp(self):
        self.browser = Client()

        ''' ROOT WORK'''
        """Create a root user just needed for create 2 degree and add 2 subjects to each degree"""
        self.test_root = UserProfile.objects.create(email='root@root.root',
                                                    name='root',
                                                    is_active=True,
                                                    is_staff=True,
                                                    is_superuser=True)
        self.test_root.set_password('root')
        self.test_root.save()

        ''' Login with new test user '''
        login = self.browser.post('/api/login/', {'username': 'root@root.root', 'password': 'root'})
        token = "Token " + json.loads(login.content)['token']
        self.browser.defaults['HTTP_AUTHORIZATION'] = token

        """Create 2 new degree using the degree API"""
        self.browser.post('/api/degrees/', {'name': 'TestDegree1',
                                            'approval_note': 4})

        self.browser.post('/api/degrees/', {'name': 'TestDegree2',
                                            'approval_note': 4})

        """Adding new subjects to each new degree using the subject API"""
        self.browser.post('/api/subjects/', {"id_degree": 1,
                                             "subject_name": "Test I",
                                             "semester": 1})

        self.browser.post('/api/subjects/', {"id_degree": 1,
                                             "subject_name": "Test II",
                                             "semester": 2})

        self.browser.post('/api/subjects/', {"id_degree": 2,
                                             "subject_name": "Test III",
                                             "semester": 1})

        self.browser.post('/api/subjects/', {"id_degree": 2,
                                             "subject_name": "Test IV",
                                             "semester": 2})

        """Create correlatives"""
        self.browser.post('/api/correlatives/', {"id_subject": 1,
                                                 "correlative_subject": 2
                                                 })

        self.browser.post('/api/correlatives/', {"id_subject": 3,
                                                 "correlative_subject": 4
                                                 })

        '''TEST USER (NOT ROOT) WORK'''
        """Create a new test user"""
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

        """Create a new UserDegree"""
        self.new_user_degree = self.browser.post('/api/users_degrees/', {'id_user': 2,
                                                                         'id_degree': 1})

    def test_correlatives(self):
        """Check if thw test user can see only his own correlatives from his userDegree"""

        correlatives = self.browser.get('/api/correlatives/', content_type="application/json")

        # Convert string to List
        correlatives_list = correlatives.json()

        # Convert List to dict
        subject_name = correlatives_list[0].get('id_subject')
        correlative_name = correlatives_list[0].get('correlative_subject')

        # Check the assert
        self.assertEqual(subject_name, 'Test I')
        self.assertEqual(correlative_name, 'Test II')
