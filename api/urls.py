from django.urls import path
from .views import Register,Create_loan,View_loan,View_loans

urlpatterns = [
    path("register",Register,name="register"),
    path("create-loan",Create_loan,name="create_loan"),
    path("view-loan/<str:loan_id>",View_loan,name="view_loan"),
    path("view-loans/<str:customer_id>",View_loans,name="view_loans")
]