from django.shortcuts import render
from rest_framework.views import APIView
import datetime
from expenses.models import Expense
from rest_framework import status, response

from income.models import Income


class ExpenseSummaryStats(APIView):
    def get_category(self, expense):
        return expense.category

    def get_amount_for_category(self, expenses_list, category):
        expenses = expenses_list.filter(category = category)
        amount = 0

        for expense in expenses:
            amount += expense.amount
        
        return {'amount' : str(amount)}


    def get(self, request):
        todays_date = datetime.date.today()
        ayear_ago = todays_date - datetime.timedelta(days = 30*12)
        expenses = Expense.objects.filter(owner = request.user, date__gte = ayear_ago, date__lte = todays_date)
       

        final = {}
        #set for remove duplicate -- map for loop and convert to list
        categories = set(map(self.get_category , expenses))
    
        for expense in expenses:
            for category in categories:
                final[category]= self.get_amount_for_category(expenses, category)
        return response.Response({
            'category_data': final
        }, status = status.HTTP_200_OK)


###############################################################################


class IncomeSourcesSummaryStats(APIView):
    def get_source(self, income):
        return income.source

    def get_amount_for_source(self, income_list, source):
        incomes = income_list.filter(source = source)
        amount = 0

        for income in incomes:
            amount += income.amount
        
        return {'amount' : str(amount)}


    def get(self, request):
        todays_date = datetime.date.today()
        ayear_ago = todays_date - datetime.timedelta(days = 30*12)
        incomes = Income.objects.filter(owner = request.user, date__gte = ayear_ago, date__lte = todays_date)
       

        final = {}
        #set for remove duplicate -- map for loop and convert to list
        sources = set(map(self.get_source , incomes))
    
        for income in incomes:
            for source in sources:
                final[source]= self.get_amount_for_source(incomes, source)
        return response.Response({
            'income_data': final
        }, status = status.HTTP_200_OK)

