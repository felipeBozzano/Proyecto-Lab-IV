from django.test import TestCase, Client
import json

from users.models import UserProfile


class SubjectTest(TestCase):

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

        """Create a new subject using the subject API"""
        self.new_subject = self.browser.post('/api/subjects/', {"id_degree": 1,
                                                                "subject_name": "Test I",
                                                                "semester": 5})

        '''Convert byte object to string'''
        self.string_new_subject = self.new_subject.content.decode("utf-8").replace("'", '"')

        '''Convert string_new_subject to dict_new_subject'''
        self.dict_new_subject = json.loads(self.string_new_subject)
        self.new_subject_name = self.dict_new_subject.get('subject_name')
        self.new_subject_id_degree = self.dict_new_subject.get('id_degree')
        self.new_subject_semester = self.dict_new_subject.get('semester')

    def test_subject_data(self):
        """Verify correct degree data"""

        # Get all the degrees
        selected_subject = self.browser.get('/api/subjects/', content_type="application/json")

        # Convert string to List
        temporalList = selected_subject.json()

        # Convert List to dict
        subject_name = temporalList[0].get('subject_name')
        subject_id_degree = temporalList[0].get('id_degree')
        subject_semester = temporalList[0].get('semester')

        # Check the assert
        self.assertEqual(subject_name, self.new_subject_name)
        self.assertEqual(subject_id_degree, self.new_subject_id_degree)
        self.assertEqual(subject_semester, self.new_subject_semester)
