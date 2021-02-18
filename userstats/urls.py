from django.urls import path
from . import views


urlpatterns = [
    path('expense_category_data/', views.ExpenseSummaryStats.as_view(), name="expense_category_data"),
    path('income_source_data/', views.IncomeSourcesSummaryStats.as_view(), name="income_source_data"),
   
]
