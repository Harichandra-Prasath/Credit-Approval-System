from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer,Loan
import json

# Create your views here.

@api_view(["POST"])
def Register(request):
    post_data = request.data
    try:
        customer = Customer.objects.create(
            first_name = post_data["first_name"],
            last_name = post_data["last_name"],
            age = post_data["age"],
            monthly_salary = post_data["monthly_income"],
            phone_number = post_data["phone_number"]
        )
        customer.save()
        response = {
            "customer_id": customer.pk,
            "name": customer.full_name(),
            "age":customer.age,
            "monthly_income": customer.monthly_salary,
            "approved_limit":customer.approved_limit,
            "phone_number":int(customer.phone_number)
        }
        return Response(response,status=200)
    except:
        return Response({"Status":"Error","Message":"Bad request.Check your request body"},status=400)

    
@api_view(["POST"])
def Create_loan(request):
    post_data = request.data
    try:
        try:
            customer = Customer.objects.get(pk=post_data["customer_id"])
        except:
            return Response({"Status":"Error","Message":"Error Fetching Customer. Check your request body"},status=400)
        loan = Loan(
            customer= customer,
            amount= post_data["loan_amount"],
            interest_rate = post_data["interest_rate"],
            tenure = post_data["tenure"]
        )
        loan.save()
        response = {
            "loan_id":loan.pk,
            "customer_id":loan.customer.pk,
            "loan_approved":True,
            "message": "Loan Approved",
            "monthly_installment": loan.emi
        }

        return Response(response,status=200)
    except:
        return Response({"Status":"Error","Message":"Bad request.Check your request body"},status=400)
    

@api_view(["GET"])
def View_loan(request,loan_id):
    try:
        loan = Loan.objects.get(pk=loan_id)
    except:
        return Response({"Status":"Error","Message":"Invalid Loan Id. Request not found"},status=404)
    
    _customer_details = {
        "first_name": loan.customer.first_name,
        "last_name": loan.customer.last_name,
        "phone_number": int(loan.customer.phone_number) ,
        "age": loan.customer.age
    }

    response = {
        "loan_id":loan_id,
        "customer":_customer_details,
        "loan_amount":loan.amount,
        "interest_rate":loan.interest_rate,
        "monthly_installment":loan.emi,
        "tenure":loan.tenure
    }
    return Response(response,status=200)