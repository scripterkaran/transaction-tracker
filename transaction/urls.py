from django.urls import include
from django.urls import path
from .views import TransactionListView, TransactionAddView, TransactionDetailView, \
    CategoryListView, CategoryAddView, CategoryDetailView

category_urlpatterns = [
    path('category/', CategoryListView.as_view(), name="category-list"),
    path('category/add/', CategoryAddView.as_view(), name="category-add"),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),
]

urlpatterns = [
    path('transactions/', TransactionListView.as_view(), name="transaction-list"),
    path('transactions/add/', TransactionAddView.as_view(), name="transaction-add"),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name="transaction-detail"),
    path('', include(category_urlpatterns)),
]
