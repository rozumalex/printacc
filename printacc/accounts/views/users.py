from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import authenticate

from ..permissions import IsAdmin, IsDealer, IsAnnonymous
from ..models import User, Account
from ..serializers import AccountsSerializer, LoginSerializer


class UsersListView(generics.ListAPIView):
    permission_classes = (IsDealer, IsAdmin,)
    queryset = Account.objects.users().all()
    serializer_class = AccountsSerializer


class UsersCreateView(generics.CreateAPIView):
    permission_classes = (IsAnnonymous,)
    serializer_class = AccountsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"token": user.auth_token.key})


class UsersLoginView(generics.CreateAPIView):
    permission_classes = (IsAnnonymous,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong Credentials'})


class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsDealer, IsAdmin,)
    queryset = User.objects.all()
    serializer_class = AccountsSerializer
