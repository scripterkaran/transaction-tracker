from django.urls import path
from .views import SignUp

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', auth_views.login, name="login"),
    path('logout/', auth_views.logout, name="logout"),
]
