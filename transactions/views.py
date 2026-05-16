from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from .models import Transaction
from .serializers import TransactionSerializer
from .filters import TransactionFilter

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = TransactionFilter
    search_fields = ['note']
    ordering_fields = ['date', 'amount', 'created_at']

    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user
        ).select_related('category')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


