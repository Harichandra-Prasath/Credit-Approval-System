from .response import view_loans_element_response

def generate_response(loans):
    response = []
    for loan in loans:
        _response = view_loans_element_response(loan)
        response.append(_response)   
    return response

def is_eligible():
    pass