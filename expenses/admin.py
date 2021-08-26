from django.contrib import admin

from expenses.models import Category, Expense

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'account', 'price', 'date_created')
    search_fields = ('title', 'account')
    list_filter = ('category', 'price')