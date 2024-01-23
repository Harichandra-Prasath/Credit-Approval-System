from .response import view_loans_element_response
import datetime

def generate_response(loans):
    response = []
    for loan in loans:
        _response = view_loans_element_response(loan)
        response.append(_response)   
    return response

def is_eligible(customer):
    loans = customer.loans.all()
    credit_score = 0
    total_loan = 0
    total_tenures = 0
    total_paid_on_time = 0
    total_emis = 0

    for loan in loans:
         total_emis+= loan.emi
    if total_emis>customer.monthly_salary*0.5:
         return False,None,"Current Emi exceeds 50 percent of monthly salary"

    # Sum of current loans vs approved limit
    for loan in loans:
        total_loan+= loan.amount
    if total_loan>customer.approved_limit:
        return False,None,"Total Loan amount exceeds Approved limit"    
    else:
        if total_loan<(customer.approved_limit*0.3):    # less than 30% , full score
            credit_score+= 20
        elif total_loan<(customer.approved_limit*0.5):  # less than 50%, 10
            credit_score+= 10
        elif total_loan<(customer.approved_limit*0.7):   #less than 70% , 5
            credit_score+= 5
    
    # dues paid on time
    for loan in loans:
        total_tenures+=loan.tenure
        total_paid_on_time+=loan.paid_on_time      # 80% of dues are paid on time
    if total_paid_on_time>total_tenures*0.8:    
            credit_score+= 20
    elif total_paid_on_time>total_tenures*0.5:   # 50% of dues are paid on time
            credit_score+= 10
    elif total_paid_on_time>total_tenures*0.3:    # 30% of dues are paid on time
            credit_score+= 5
    

    #no of loans
            
    if len(loans)<3:
        credit_score+=20
    elif len(loans)<5:
        credit_score+=10
    else:
        credit_score+=5
    
    # loan approval volume
    flag = 0

    for loan in loans:
         if loan.amount>customer.approved_limit*0.5:    #high volume loan is processed
            credit_score+= 20
            flag = 1
            break
    if flag==0:
         credit_score+=10           # No high volume loan is processed
    

    # loan activity in this year
    current_year_loans = 0
    current_year = str(datetime.date.today()).split("-")[0]
    for loan in loans:
        if str(loan.start_date).split("-")[0]==current_year:
             current_year_loans+=1
    
    if current_year_loans>2:
         credit_score+=5
    elif current_year_loans>0:
         credit_score+=10
    else:
         credit_score+=20
    
    # Following the credit-system
    if credit_score>50:
         return True,None,"Loan Approved.Approved for requested interest rate"
    elif 30<credit_score<50:
         return True,12,"Loan Approved. Approved with 12 percent interest rate"
    elif 10<credit_score<30:
         return True,16,"Loan Approved. Approved with 16 percent interest rate"
    else:
         return False,None,"Credit Score less than 10"