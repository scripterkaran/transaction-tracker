from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import render, redirect


class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'core/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('transaction-list')
        return render(request, 'core/signup.html', {'form': form})
