
# Response template for the Register View
def Register_response(customer):
    return {
            "customer_id": customer.pk,
            "name": customer.full_name(),
            "age":customer.age,
            "monthly_income": customer.monthly_salary,
            "approved_limit":customer.approved_limit,
            "phone_number":int(customer.phone_number)
            }

# Response template for the Create-loan View
def create_loan_response(loan):
    return {
            "loan_id":loan.pk,
            "customer_id":loan.customer.pk,
            "loan_approved":True,
            "message": "Loan Approved",
            "monthly_installment": loan.emi
        }

# Response template for the View-loan View
def view_loan_response(loan):

    # Building the customer context
    _customer_details = {
        "first_name": loan.customer.first_name,
        "last_name": loan.customer.last_name,
        "phone_number": int(loan.customer.phone_number) ,
        "age": loan.customer.age
    }

    return  {
        "loan_id":loan.pk,
        "customer":_customer_details,
        "loan_amount":loan.amount,
        "interest_rate":loan.interest_rate,
        "monthly_installment":loan.emi,
        "tenure":loan.tenure
    }

# Response template for view-loans individual elements 
def view_loans_element_response(loan):
    return {
            "loan_id":loan.id,
            "loan_amount":loan.amount,
            "interest_rate":loan.interest_rate,
            "monthly_installment":loan.emi,
            "repayments_left":loan.repayments_left()
        }