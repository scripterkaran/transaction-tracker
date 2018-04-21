from django import forms
from .models import Transaction, Category


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'transaction_type', 'value', 'category']

class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]

