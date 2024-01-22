from django.db import models

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
            _approved_limit = 36*self.monthly_salary/100000
            _rounder_limit = ((36*self.monthly_salary//100000) if _approved_limit%1 <0.5
                            else (36*self.monthly_salary//100000)+1)
            self.approved_limit = _rounder_limit*100000
        super().save(*args,**kwargs)