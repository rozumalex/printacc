from rest_framework import generics

from ..permissions import IsAdmin, IsDealer
from ..models import Account
from ..serializers import AccountsSerializer


class DealersListView(generics.ListAPIView):
    permission_classes = (IsAdmin,)
    queryset = Account.objects.dealers().all()
    serializer_class = AccountsSerializer


class DealersDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdmin, IsDealer)
    queryset = Account.objects.dealers().all()
    serializer_class = AccountsSerializer
