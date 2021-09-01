from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Account
from users.permissions import IsOwner
from .serializers import AccountRegistrationSerializer, AccountDetailSerializer
from rest_framework import generics, permissions, status


class AccountRegisterAPIView(generics.CreateAPIView):

    """
    This endpoint registers users based on the fields
    """

    serializer_class = AccountRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

class AccountDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

