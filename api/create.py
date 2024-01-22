# Additional file to handle model creations and to handle errors
from .models import Customer,Loan

def create_Customer_instance(data):
    try:
        customer = Customer.objects.create(
            first_name = data["first_name"],
            last_name = data["last_name"],
            age = data["age"],
            monthly_salary = data["monthly_income"],
            phone_number = data["phone_number"]
        )
        customer.save()
        return True,customer
    except:
        return False,None

def create_Loan_instance(data,customer):
    try:
        loan = Loan(
            customer= customer,
            amount= data["loan_amount"],
            interest_rate = data["interest_rate"],
            tenure = data["tenure"]
        )
        loan.save()
        return True,loan
    except:
        return False,None