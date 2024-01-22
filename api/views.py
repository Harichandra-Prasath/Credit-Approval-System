from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer

# Create your views here.

@api_view(["POST"])
def Register(request):
    post_data = request.data

    try:
        customer = Customer.objects.create(
            first_name = post_data["first_name"],
            last_name = post_data["last_name"],
            age = int(post_data["age"]),
            monthly_salary = int(post_data["monthly_income"]),
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

    
