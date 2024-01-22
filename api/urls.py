from django.urls import path
from .views import *

urlpatterns = [
    path("register",Register,name="register"),
    path("create-loan",Create_loan,name="create_loan"),
    path("view-loan/<str:loan_id>",View_loan,name="view_loan")
]