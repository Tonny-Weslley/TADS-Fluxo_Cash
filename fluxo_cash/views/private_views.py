from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View


class App(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/dashboard.html')


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')
