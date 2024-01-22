from django.test import TestCase
from django.urls import reverse
import json

class RegisterViewTest(TestCase):

    def test_register(self):
        post = {
            "first_name":"hari",
            "last_name": "prasath",
            "age":25,
            "monthly_income":47000,
            "phone_number": 9878980998
        }
        response_exp = {
            "customer_id":1,
            "name":"hari prasath",
            "age":25,
            "monthly_income":47000,
            "approved_limit":1700000,
            "phone_number": 9878980998
        }
        _response = self.client.post(reverse("register"),post)
        response = json.loads(_response.content)
        self.assertEqual(response,response_exp)        