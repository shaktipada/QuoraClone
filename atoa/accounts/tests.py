from django.test import TestCase
from django.utils import unittest
from django.test.client import Client
from django.core.urlresolvers import reverse

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        del self.client


    def test_res(self):

        # Issue a GET request.
        response = self.client.get(reverse(’profile_page’))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse(’login_page’))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse(’home_page’))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse(’logout_page’))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse(’question_page’))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse(’questions_page’))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse(’my_questions_page’))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse(’del_answer_page’))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse(’del_answer_page’))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse(’edit_answer’))
        self.assertEqual(response.status_code, 200)



        """ response = self.client.post(
            '/LoginPage/login',
            {
                'username': 'a', 'password': 'aa'
            })

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['form'].errors), 0)

    def test_profile_page(self):

        response = self.client.get(reverse(’profile_page’))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('profile_page')
            {
                'username': 'xyz', 'password': 'abc',
                'first_name': 'abc', 'last_name': 'xyz',
                'email': 'abc@xyz.com'
            })
        self.assertEqual(response.status_code, 200)"""