from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Budget
from .serializers import BudgetSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Budget.objects.none()

        queryset = Budget.objects.filter(
            user=self.request.user
        ).select_related('category')

        month = self.request.query_params.get('month')
        if month:
            try:
                from datetime import datetime
                date = datetime.strptime(month, '%Y-%m')
                queryset = queryset.filter(
                    month__year=date.year,
                    month__month=date.month,
                )
            except ValueError:
                pass

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)