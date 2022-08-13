from django.shortcuts import redirect, render
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('app')
        return render(request, 'public/index.html')


class Login(View):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('app')
        return render(request, 'public/login.html')


class Register(View):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('app')
        return render(request, 'public/register.html')
