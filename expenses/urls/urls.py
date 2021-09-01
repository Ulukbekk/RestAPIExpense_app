from django.urls import path
from expenses.views import BalanceIncreaseAPIView
from .routers import urlpatterns as routers

urlpatterns = [
    path('balance/top-up/', BalanceIncreaseAPIView.as_view())
]

urlpatterns += routers













# from .views import ( expense_create_view,
#                      expenses_list_api_view,
#                      expense_retrieve_api_view,
#                      expense_put_update_api_view,
#                      expense_delete )
#########################################
# from expenses.views import ExpenseCreateAPIView, ExpenseListAPIView, ExpenseRetrieveAPIView, ExpenseUpdateAPIView, \
#     ExpenseDeleteAPIView
######################################
# urlpatterns = [
#     path('<int:pk>/', ExpenseRetrieveUpdateDeleteAPIView.as_view()),
#     path('', ExpenseListCreateAPIView.as_view()),
# ]
#######################################################3
# urlpatterns = [
#     path('create/', ExpenseCreateAPIView.as_view()),
#     path('list/', ExpenseListAPIView.as_view()),
#     path('expense/<int:pk>/', ExpenseRetrieveAPIView.as_view()),
#     path('expense-update/<int:pk>/', ExpenseUpdateAPIView.as_view()),
#     path('expense-delete/<int:pk>/', ExpenseDeleteAPIView.as_view()),
# ]
####################################################################3
# urlpatterns = [
#     path('create/', expense_create_view
#          , name='expense_create'),
#     path('list/', expenses_list_api_view, name='expenses_list'),
#     path('expense/<int:pk>/', expense_retrieve_api_view, name='expense_detail'),
#     path('expense-delete/<int:pk>/', expense_delete, name='expense_delete'),
#     path('expense-update/<int:pk>/', expense_put_update_api_view, name='expense_update'),
# ]