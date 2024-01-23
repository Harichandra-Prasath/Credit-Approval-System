from django.core.management.base import BaseCommand
import pandas as pd
from api.models import Customer,Loan,Dummy

class Command(BaseCommand):
    help = "To populate the database"
    def handle(self,*args,**kwargs):
        customers = pd.read_excel("customer_data.xlsx")
        loans = pd.read_excel("loan_data.xlsx")

        for _,row in customers.iterrows():

            Customer.objects.create(
                pk=row['Customer ID'],
                first_name=row['First Name'],
                last_name=row['Last Name'],
                age=row['Age'],
                phone_number=str(row['Phone Number']),
                monthly_salary=row['Monthly Salary'],
                approved_limit=row['Approved Limit']
            ).save()
        
        for _,row in loans.iterrows():
            # Try to create loans , if found duplicates , then pass
            try: 
                Loan.objects.create(
                    customer= Customer.objects.get(pk=row['Customer ID']),
                    pk=row['Loan ID'],
                    amount=row['Loan Amount'],
                    tenure=row['Tenure'],
                    interest_rate=row['Interest Rate'],
                    emi=row['Monthly payment'],
                    paid_on_time=row['EMIs paid on Time'],
                    start_date=row['Date of Approval'],
                    end_date=row['End Date']
                ).save()
            except:                 # there are duplicated loan ids in the file
                continue 
        Dummy.objects.create().save()
        self.stdout.write(self.style.SUCCESS('Database has been populated successfully'))
