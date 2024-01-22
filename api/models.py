from django.db import models
import datetime

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=36,null=False)
    last_name = models.CharField(max_length=36,null=False)
    age = models.IntegerField(default=18)
    phone_number = models.CharField(max_length=10,null=False) # to avoid the out of range for integers
    monthly_salary = models.IntegerField(null=False)
    approved_limit = models.IntegerField(null=False)
    current_debt = models.IntegerField(default=0,null=False)

    def full_name(self):
        return self.first_name+" "+ self.last_name

    def save(self,*args,**kwargs):
        if not self.approved_limit:
            _approved_limit = 36*self.monthly_salary/100000  #To get number of lakhs

            # if 7.2 ---> 7 else 7.9 ---> 8  rounding to the nearest lakhs
            _rounder_limit = ((36*self.monthly_salary//100000) if _approved_limit%1 <0.5
                            else (36*self.monthly_salary//100000)+1)
      
            self.approved_limit = _rounder_limit*100000   
        super().save(*args,**kwargs)


class Loan(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="loans")
    amount = models.FloatField(null=False)
    tenure = models.IntegerField(null=False)
    interest_rate = models.FloatField(null=False)
    emi = models.FloatField(null=False)
    paid_on_time = models.IntegerField(null=False,default=0)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=False)

    def save(self,*args,**kwargs):

        # Calculating the end_date based on tenure 
        if not self.end_date:
            self.end_date = datetime.date.today() + datetime.timedelta(days=365.2425*self.tenure)
        
        # Calculating emi using amortization formula
        if not self.emi:
            _r = (self.interest_rate/(12*100))
            n = self.tenure * 12
            _r_term =  (1+_r)**n
            self.emi = float("%.2f"%(self.amount * (_r*_r_term/(_r_term-1))))
        super().save(*args,**kwargs)
