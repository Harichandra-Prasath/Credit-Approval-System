from django.test import TestCase
from django.urls import reverse
import json
from api.models import Customer,Loan

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
        _response = self.client.post(reverse("register"),post,content_type="application/json")
        response = json.loads(_response.content)
        self.assertEqual(response,response_exp)

class LoanCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        customer = Customer(
            first_name="hari",
            last_name = "prasath",
            phone_number = "9789878909",
            monthly_salary = 47000,
            age = 25
        )
        customer.save()

        loan = Loan(
            customer = customer,
            amount = 10000,
            tenure = 36,
            interest_rate=5,
        )
        loan.save()

    def test_create_loan(self):
        post = {
            "customer_id":1,
            "loan_amount": 10000,
            "tenure": 36,
            "interest_rate":5
        }
        response_exp = {
            "loan_id":2,
            "customer_id":1,
            "loan_approved":True,
            "message":"Loan Approved",
            "monthly_installment":299.71
        }
        _response = self.client.post(reverse("create_loan"),post,content_type="application/json")
        response = json.loads(_response.content)
        self.assertEqual(response,response_exp)
    
    def test_view_loan(self):
        _response = self.client.get(reverse("view_loan",kwargs={"loan_id":1}))
        self.assertEqual(_response.status_code,200)
    
    def test_view_loans(self):
        _response = self.client.get(reverse("view_loans",kwargs={"customer_id":1}))
        response = json.loads(_response.content)
        self.assertEqual(_response.status_code,200)
        self.assertEqual(len(response["Loans"]),1)