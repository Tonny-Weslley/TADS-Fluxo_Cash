from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app')
        return render(request, 'public/login.html', context={'error': 'User or password invalid'})


class Register(View):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('app')
        return render(request, 'public/register.html')

    def post(self, request, *args, **kwargs):
        # verificando campos vazios
        verified = True
        errors = {}
        for attribute in request.POST:
            if(request.POST[attribute] == ''):
                verified = False
                errors[attribute] = 'empty'
        # verifying if password and confirm password are equal
        if(request.POST['password'] != request.POST['password-confirm']):
            verified = False
            errors['passwords'] = 'not_equal'

        # verifying if user already exists
        if(User.objects.filter(username=request.POST['username']).exists()):
            verified = False
            errors['user'] = 'exists'

        if(verified):
            user = User.objects.create_user(
                request.POST['username'], request.POST['email'], request.POST['password'])
            user.first_name = request.POST['first-name']
            user.last_name = request.POST['last-name']
            user.save()
            return redirect('login')
        else:
            context = {'errors': errors}
            return render(request, 'public/register.html', context)
