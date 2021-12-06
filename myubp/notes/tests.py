from django.test import TestCase, Client
import json

from users.models import UserProfile


class NoteTest(TestCase):

    def setUp(self):
        self.browser = Client()

        ''' ROOT WORK'''
        """Create a root user just needed for create a degree and add subjects to that degree"""
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

        """Create a new degree using the degree API"""
        self.new_degree = self.browser.post('/api/degrees/', {'name': 'TestDegree',
                                                              'approval_note': 4}, HTTP_AUTHORIZATION=token)

        """Create a new subject using the subject API"""
        self.new_subject_1 = self.browser.post('/api/subjects/', {"id_degree": 1,
                                                                  "subject_name": "Test I",
                                                                  "semester": 1}, HTTP_AUTHORIZATION=token)

        """Create another subject using the subject API"""
        self.new_subject_2 = self.browser.post('/api/subjects/', {"id_degree": 1,
                                                                  "subject_name": "Test II",
                                                                  "semester": 2}, HTTP_AUTHORIZATION=token)

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
                                                                         'id_degree': 1}, HTTP_AUTHORIZATION=self.token,
                                                 content_type="application/json")

        '''Add Notes to both new subjects'''
        self.browser.post('/api/notes/', {
                                            "id_user": 2,
                                            "id_subject": 1,
                                            "exam_note": 7
                                        }, HTTP_AUTHORIZATION=token)

        self.exam_note = self.browser.get('/api/notes/1/',  content_type="application/json")

        '''Convert byte object to string'''
        self.string_new_exam_note = self.exam_note.content.decode("utf-8").replace("'", '"')

        '''Convert string_new_exam_note to dict_new_exam_note'''
        self.dict_new_exam_note = json.loads(self.string_new_exam_note)

        self.new_exam_note = self.dict_new_exam_note.get('exam_note')
        self.new_exam_note_user_id = self.dict_new_exam_note.get('id_user')
        self.new_exam_note_subject_id = self.dict_new_exam_note.get('id_subject')

        self.new_subject = self.browser.post('/api/notes/', {
                                                                "id_user": 2,
                                                                "id_subject": 2,
                                                                "exam_note": 9
                                                            }, HTTP_AUTHORIZATION=token)

    def test_update_exam_note(self):
        """Update exam note and check for the correct update value"""

        # Updating one note
        updated = self.browser.put('/api/notes/1/', {
                                                        "id": 1,
                                                        "id_user": 2,
                                                        "id_subject": 1,
                                                        "exam_note": 9
                                                    }, HTTP_AUTHORIZATION=self.token, content_type="application/json")

        updated_note = self.browser.get('/api/notes/1/',  content_type="application/json")

        # Convert string to List
        list_note = updated_note.json()

        # Convert List to dict
        updated_exam_note = list_note.get('exam_note')
        updated_subject_id = list_note.get('id_subject')
        updated_user_id = list_note.get('id_user')

        # Check the assert
        self.assertNotEqual(updated_exam_note, self.new_exam_note)
        self.assertEqual(updated_exam_note, 9)
        self.assertEqual(updated_subject_id, self.new_exam_note_subject_id)
        self.assertEqual(updated_user_id, self.new_exam_note_user_id)

    def test_get_avg_note(self):
        """Get exam notes average"""

        avg_note = self.browser.get('/api/notes-avg/',  content_type="application/json")

        # Convert string to List
        list_avg = avg_note.json()

        # Convert List to dict
        dict_avg_note = list_avg[0].get('average_note')

        # Check the assert
        self.assertEqual(dict_avg_note, 8)
