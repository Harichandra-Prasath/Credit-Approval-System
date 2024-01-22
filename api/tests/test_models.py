from django.test import TestCase

from api.models import Customer,Loan

class CustomerModelTest(TestCase):

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

    
    def test_approved_limit(self):
        customer = Customer.objects.get(pk=1)      
        self.assertEqual(customer.approved_limit,1700000)


    def test_default_debt(self):
        customer = Customer.objects.get(pk=1)
        self.assertEqual(customer.current_debt,0)
    
    def test_full_name(self):
        customer = Customer.objects.get(pk=1)
        self.assertEqual(customer.full_name(),"hari prasath")


class LoanModelTest(TestCase):

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
            tenure = 3,
            interest_rate=5,
        )
        loan.save()
    
    def test_default_paid_ont_time(self):
        loan = Loan.objects.get(pk=1)
        self.assertEqual(loan.paid_on_time,0)
    
    def test_loan_customer(self):
        loan = Loan.objects.get(pk=1)
        customer = loan.customer
        self.assertEqual(customer.pk,1)
    
    def test_loan_emi(self):
        loan = Loan.objects.get(pk=1)
        self.assertEqual(float("%.2f"%loan.emi),299.71)
    
    def test_check_customer_loan(self):
        customer = Customer.objects.get(pk=1)
        self.assertEqual(len(customer.loans.all()),1)
        self.assertEqual(customer.loans.get(pk=1).amount,10000)
