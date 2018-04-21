from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView

from .forms import TransactionForm, CategoryAddForm
from .models import Transaction, Category


class TransactionListView(ListView):
    model = Transaction

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TransactionListView, self).dispatch(request, *args, **kwargs)
    
class TransactionAddView(CreateView):
    model = Transaction
    form_class = TransactionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionDetailView(DetailView):
    model = Transaction


class CategoryListView(ListView):
    model = Category

class CategoryAddView(CreateView):
    model = Category
    form_class = CategoryAddForm

    def get_success_url(self):
        return reverse('transaction-list')

class CategoryDetailView(DetailView):
    model = Category


