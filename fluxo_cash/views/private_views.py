from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View


class App(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/dashboard.html')
