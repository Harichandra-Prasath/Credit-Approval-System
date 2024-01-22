from django.test import TestCase

from api.models import Customer

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