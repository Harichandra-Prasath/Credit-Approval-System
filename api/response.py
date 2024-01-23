# File containing all the response templates


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
def create_loan_response(loan,message):
    return {
            "loan_id":loan.pk,
            "customer_id":loan.customer.pk,
            "loan_approved":True,
            "message": message,
            "monthly_installment": loan.emi
        }

# Response template for the Failed-loan View
def failed_loan_response(customer,message):
    return {
            "loan_id":"-",
            "customer_id":customer.pk,
            "loan_approved":False,
            "message": message,
            "monthly_installment": "-"
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
            "loan_id":loan.pk,
            "loan_amount":loan.amount,
            "interest_rate":loan.interest_rate,
            "monthly_installment":loan.emi,
            "repayments_left":loan.repayments_left()
        }


# Response template for eligibility individual elements 
def Eligible_response(post_data,eligible,corrected_interest,emi):
    return {
            "customer_id":post_data['customer_id'],
            "approval": eligible,
            "interest_rate":post_data['interest_rate'],
            "corrected_interest_rate": post_data['interest_rate'] if not corrected_interest else corrected_interest,
            "tenure":post_data['tenure'],
            "monthly_installment":emi
        }