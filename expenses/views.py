from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from expenses.models import Expense, Category
from expenses.permissions import IsOwner
from expenses.serializers import ExpenseSerializer, ExpenseDetailSerializer, CategoryDetailSerializer
from expenses.services import TopUpService
from expenses.validators import TopUpValidator
from users.models import Account
from rest_framework import generics, permissions

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)

class CategoryDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()

class BalanceIncreaseAPIView(generics.GenericAPIView):
    validator_class = TopUpValidator
    service_class = TopUpService
    def post(self, request, *args, **kwargs):
        balance = request.data.get('balance')
        if not self.validator_class.validator_balance(balance):
            return Response('Pass balance to top-up', status=status.HTTP_400_BAD_REQUEST)
        self.service_class.top_up(request.user, balance)
        return Response('Ok', status=status.HTTP_200_OK)
# class ExpenseListCreateAPIView(generics.ListCreateAPIView):
#     """
#     This endpoint creates on expense to logged in user
#     or gives a list of available expensesx
#     """
#     serializer_class = ExpenseSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(account=self.request.user.account)
#
#     def get_queryset(self):
#         return Expense.objects.filter(account=self.request.user.account)
#
# class ExpenseRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwner)
###################################################
# class ExpenseCreateAPIView(generics.CreateAPIView):
#     serializer_class = ExpenseSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def perform_create(self, serializer):
#         serializer.save(account=self.request.user.account)
#
# class ExpenseListAPIView(generics.ListAPIView):
#     serializer_class = ExpenseSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get_queryset(self):
#         return Expense.objects.filter(account=self.request.user.account)
#
# class ExpenseRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseDetailSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwner)
#
# class ExpenseUpdateAPIView(generics.UpdateAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwner)
#
# class ExpenseDeleteAPIView(generics.DestroyAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwner)
#
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response('Deleted',status=status.HTTP_204_NO_CONTENT)

##########################################################################
# @csrf_exempt
# @api_view(['POST'])
# def expense_create_view(request):
#     if request.method == 'POST':
#         category_id = request.POST.get('category')
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         user = request.user
#         account = Account.objects.filter(user=user).first()
#         category = Category.objects.filter(id=category_id).first()
#         expense = Expense.objects.create(
#             category=category,
#             title=title,
#             description=description,
#             price=price,
#             account=account
#         )
#
#     return HttpResponse(expense, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def expenses_list_api_view(request):
#     user = request.user
#     account = Account.objects.filter(user=user).first()
#     account_expenses = Expense.objects.filter(account=account)
#
#     serializer = ExpenseSerializer(account_expenses, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def expense_retrieve_api_view(request, pk):
#     expense = Expense.objects.filter(id=pk).first()
#
#     if expense.account.user != request.user:
#         return Response({'Success': False,
#                          "message":"You don't have permission to access this object"},
#                         status=status.HTTP_403_FORBIDDEN)
#
#     serializer = ExpenseSerializer(expense)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def expense_put_update_api_view(request, pk):
#     expense = Expense.objects.filter(id=pk).first()
#
#     if expense.account.user != request.user:
#         return Response({'Success': False,
#                          "message": "You don't have permission to access this object"},
#                         status=status.HTTP_403_FORBIDDEN)
#     category = Category.objects.filter(id=request.data.get('category')).first()
#     print(category)
#     expense.category = category
#     expense.title = request.data.get('title')
#     expense.price = request.data.get('price')
#     expense.description = request.data.get('description')
#     expense.save()
#     print(request.data)
#     return Response(data='OK', status=status.HTTP_200_OK)
#
#
# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def expense_delete(request, pk):
#     expense = Expense.objects.filter(id=pk).first()
#     if expense.account.user != request.user:
#         return Response({'Success': False,
#                          "message": "You don't have permission to access this object"},
#                         status=status.HTTP_403_FORBIDDEN)
#     expense.delete()
#     return Response('Deleted', status=status.HTTP_200_OK)
