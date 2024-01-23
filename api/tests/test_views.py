from django.test import TestCase
from django.urls import reverse
import json
from api.models import Customer,Loan,Dummy
from api.utils import is_eligible

class RegisterViewTest(TestCase):

    def test_register(self):
        post = {
            "first_name":"hari",
            "last_name": "prasath",
            "age":25,
            "monthly_income":47000,
            "phone_number": 9878980998
        }
        _response = self.client.post(reverse("register"),post,content_type="application/json")
        response_exp = {
            "customer_id":Customer.objects.last().pk,
            "name":"hari prasath",
            "age":25,
            "monthly_income":47000,
            "approved_limit":1700000,
            "phone_number": 9878980998
        }
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
            "customer_id":Customer.objects.last().pk,
            "loan_amount": 10000,
            "tenure": 36,
            "interest_rate":5
        }
        _response = self.client.post(reverse("create_loan"),post,content_type="application/json")
        response_exp = {
            "loan_id":Loan.objects.last().pk,
            "customer_id":Customer.objects.last().pk,
            "loan_approved":True,
            "message":"Loan Approved.Approved for requested interest rate",
            "monthly_installment":299.71
        }
        response = json.loads(_response.content)
        self.assertEqual(response,response_exp)
    
    def test_view_loan(self):
        _response = self.client.get(reverse("view_loan",kwargs={"loan_id":Loan.objects.last().pk}))
        self.assertEqual(_response.status_code,200)
    
    def test_view_loans(self):
        _response = self.client.get(reverse("view_loans",kwargs={"customer_id":Customer.objects.last().pk}))
        response = json.loads(_response.content)
        self.assertEqual(_response.status_code,200)
        self.assertEqual(len(response["Loans"]),1)


class CheckEligibleTest(TestCase):
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
    
    def test_no_approval(self):
        customer = Customer.objects.latest('pk')
        loan = Loan(
            customer = customer,
            amount = 1000000,
            tenure = 36,
            interest_rate=0.05,
        )
        loan.save()
        loan2 = Loan(
            customer = customer,
            amount = 900000,
            tenure = 36,
            interest_rate=0.05,
        )
        loan2.save()
        eligible,interest,_ = is_eligible(customer)
        self.assertFalse(eligible)

    def test_approval(self):
        customer = Customer.objects.latest('pk')
        loan = Loan(
            customer = customer,
            amount = 500000,
            tenure = 50,
            interest_rate=0.005,
        )
        loan.paid_on_time = 45
        loan.save()
        loan2 = Loan(
            customer = customer,
            amount = 500000,
            tenure = 50,
            interest_rate=0.005,
        )
        loan2.paid_on_time = 45
        loan2.save()
        eligible,interest,_  = is_eligible(customer)
        self.assertTrue(eligible)
        self.assertEqual(interest,None)

