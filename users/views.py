from .models import Account
from .serializers import AccountRegistrationSerializer
from rest_framework import generics


class AccountRegisterAPIView(generics.CreateAPIView):
    serializer_class = AccountRegistrationSerializer
