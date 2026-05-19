from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from transactions.models import Transaction
import datetime


class SummaryView(APIView):
   
    permission_classes = [IsAuthenticated]

    def get(self, request):
        month_param = request.query_params.get('month')

       
        if month_param:
            try:
                date = datetime.datetime.strptime(month_param, '%Y-%m')
                year, month = date.year, date.month
            except ValueError:
                return Response({'error': 'Date format: YYYY-MM'}, status=400)
        else:
            today = datetime.date.today()
            year, month = today.year, today.month

        transactions = Transaction.objects.filter(
            user=request.user,
            date__year=year,
            date__month=month,
        )

        
        totals = transactions.values('type').annotate(total=Sum('amount'))

        income = 0
        expense = 0
        for item in totals:
            if item['type'] == 'income':
                income = item['total'] or 0
            else:
                expense = item['total'] or 0

        return Response({
            'year': year,
            'month': month,
            'total_income': income,
            'total_expense': expense,
            'balance': income - expense,
        })


class ByCategoryView(APIView):
  
    permission_classes = [IsAuthenticated]

    def get(self, request):
        month_param = request.query_params.get('month')

        if month_param:
            try:
                date = datetime.datetime.strptime(month_param, '%Y-%m')
                year, month = date.year, date.month
            except ValueError:
                return Response({'error': 'Date format: YYYY-MM'}, status=400)
        else:
            today = datetime.date.today()
            year, month = today.year, today.month

        
        data = (
            Transaction.objects
            .filter(user=request.user, date__year=year, date__month=month)
            .values('category__name', 'category__color', 'category__icon', 'type')
            .annotate(total=Sum('amount'))
            .order_by('-total')
        )

        return Response(list(data))


class MonthlyTrendView(APIView):
   
    permission_classes = [IsAuthenticated]

    def get(self, request):
        months_count = int(request.query_params.get('months', 6))

        
        data = (
            Transaction.objects
            .filter(user=request.user)
            .annotate(month=TruncMonth('date'))
            .values('month', 'type')
            .annotate(total=Sum('amount'))
            .order_by('month')
        )

        result = {}
        for item in data:
            key = item['month'].strftime('%Y-%m')
            if key not in result:
                result[key] = {'month': key, 'income': 0, 'expense': 0}
            result[key][item['type']] = item['total'] or 0

     
        trend = sorted(result.values(), key=lambda x: x['month'])
        trend = trend[-months_count:]

        return Response(trend)


class BalanceView(APIView):
   
    permission_classes = [IsAuthenticated]

    def get(self, request):
        totals = (
            Transaction.objects
            .filter(user=request.user)
            .values('type')
            .annotate(total=Sum('amount'))
        )

        income = 0
        expense = 0
        for item in totals:
            if item['type'] == 'income':
                income = item['total'] or 0
            else:
                expense = item['total'] or 0

        return Response({
            'total_income': income,
            'total_expense': expense,
            'balance': income - expense,
        })