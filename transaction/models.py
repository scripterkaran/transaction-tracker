from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % (self.name,)


class Transaction(models.Model):
    DEBIT = 1
    CREDIT = 2

    TRANSACTION_TYPE = (
        (DEBIT, 'Debit'),
        (CREDIT, 'Credit'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTION_TYPE)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="transactions")

    def get_absolute_url(self):
        return reverse('transaction-detail', kwargs={'pk': self.pk})
