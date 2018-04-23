from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, DetailView

from .forms import TransactionForm, CategoryAddForm
from .models import Transaction, Category


class Dashboard(View):

    def get(self, request, *args,**kwargs):
        if request.user.is_authenticated:
            # last 5 transactions
            transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')[:5]
            return render(request, 'transaction/dashboard.html', context={'transactions': transactions})
        else:
            return redirect('login')

class TransactionListView(ListView):
    model = Transaction

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('-created_at')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TransactionListView, self).dispatch(request, *args, **kwargs)
    
class TransactionAddView(CreateView):
    model = Transaction
    form_class = TransactionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TransactionAddView, self).dispatch(request, *args, **kwargs)

class TransactionDetailView(DetailView):
    model = Transaction

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TransactionDetailView, self).dispatch(request, *args, **kwargs)

class CategoryListView(ListView):
    model = Category

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, *args, **kwargs)

class CategoryAddView(CreateView):
    model = Category
    form_class = CategoryAddForm

    def get_success_url(self):
        return reverse('category-list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryAddView, self).dispatch(request, *args, **kwargs)

class CategoryDetailView(DetailView):
    model = Category

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDetailView, self).dispatch(request, *args, **kwargs)


