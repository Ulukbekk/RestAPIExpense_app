from django.db import models

from users.models import Account


class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural ='Categories'

    def __str__(self):
        return self.title


class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT,
                                 related_name='category_expenses', default=1)
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='user_expenses')
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

