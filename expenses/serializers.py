from rest_framework import serializers

from expenses.models import Expense, Category


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('category',
                  'title',
                  'description',
                  'price')

class ExpenseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('category',
                  'title',
                  'description',
                  'price',
                  'account',
                  'date_created')

        depth = 1

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)

