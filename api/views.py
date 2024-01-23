from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer,Loan
from .response import create_loan_response,Register_response,view_loan_response
from .utils import generate_response
from .create import create_Customer_instance,create_Loan_instance





@api_view(["POST"])
def Register(request):

    # POST Data with content type application/json
    post_data = request.data
    
    # Success indicates successful customer creation
    success,customer = create_Customer_instance(post_data)

    if success:
        response = Register_response(customer)
        return Response(response,status=200)
    else:
        return Response({"Status":"Error","Message":"Bad request.Check your request body"},status=400)

    
@api_view(["POST"])
def Create_loan(request):

    # POST Data with content type application/json
    post_data = request.data

    #Try fetching the customer
    try:
        customer = Customer.objects.get(pk=post_data["customer_id"])
    except:
        return Response({"Status":"Error","Message":"Error Fetching Customer. Check your request body"},status=400)

    # Success indicates successful Loan creation
    success,loan = create_Loan_instance(post_data,customer)

    if success:
        response = create_loan_response(loan)
        return Response(response,status=200)
    else:
        return Response({"Status":"Error","Message":"Bad request.Check your request body"},status=400)
    

@api_view(["GET"])
def View_loan(request,loan_id):
    # Trying to fetch the loan
    try:
        loan = Loan.objects.get(pk=loan_id)
    except:
        return Response({"Status":"Error","Message":"Invalid Loan Id. Request not found"},status=404)
    
    response = view_loan_response(loan)
    return Response(response,status=200)

@api_view(["GET"])
def View_loans(request,customer_id):
    #Trying to fetch the customer
    try:
        customer = Customer.objects.get(pk=customer_id)
    except:
        return Response({"Status":"Error","Message":"Invalid Customer Id.Customer not found"},status=404)
    
    loans = customer.loans.all()

    #utils function to generate the list
    loan_response = generate_response(loans) 
    
    return Response({"Loans":loan_response},status=200)

@api_view(["POST"])
def Check_eligibility(request):
    pass
