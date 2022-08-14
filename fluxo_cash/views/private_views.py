from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

from ..models import Record, Tag


class App(View):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            tags = Tag.objects.all()
            records = Record.objects.filter(
                id_userProfile=request.user.userprofile)
            context = {'tags': tags, 'records': records}
            return render(request, 'app/dashboard.html', context)
        return redirect('login')


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')


class AddRecord(View):
    def post(self, request, *args, **kwargs):
        # check if the user is authenticated
        if(request.user.is_authenticated):
            # check if the filds are empty
            valid = True
            for field in request.POST:
                if(field == ''):
                    valid = False
            if valid:
                rec_type = None
                if request.POST['type'] == '1':
                    rec_type = True
                else:
                    rec_type = False
                rec_name = request.POST['name']
                rec_value = request.POST['value']
                rec_tag = Tag.objects.get(id=request.POST['tag'])
                rec_user = request.user.userprofile
                rec = Record(name=rec_name, value=rec_value,
                             record_type=rec_type, id_tag=rec_tag, id_userProfile=rec_user)
                rec.save()
                return redirect('app')

        else:
            return redirect('login')
