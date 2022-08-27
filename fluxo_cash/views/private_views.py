from ast import Not
from http.client import HTTPResponse
from webbrowser import get

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

from ..models import Balance, Record, Tag


class App(View):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            balances = Balance.objects.filter(id_user=request.user.id)
            context = {'balances': balances}
            return render(request, 'app/dashboard.html', context)
        return redirect('login')


class AddBalance(View):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return render(request, 'app/add_balance.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        balance = Balance(id_user=request.user, name=name, value=0)
        balance.save()
        return redirect('app')


class DeleteBalance(View):
    def get(self, request, *args, **kwargs):
        balance = Balance.objects.get(id=request.GET.get('id'))
        balance.delete()
        return redirect('app')


class BalanceView(View):
    def get(self, request, *args, **kwargs):
        balance = Balance.objects.get(id=request.GET.get('id'))
        records = Record.objects.filter(
            id_balance=balance).order_by('date_in')
        tags = Tag.objects.all()
        context = {'balance': balance, 'records': records, 'tags': tags}
        return render(request, 'app/balance_viewer.html', context)


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
                balance = Balance.objects.get(id=request.POST['balance'])
                rec = Record(name=rec_name, value=rec_value,
                             record_type=rec_type, id_tag=rec_tag, id_balance=balance)
                rec.save()
                balance.ajust(rec.record_type, rec_value)

                return redirect('app')

        else:
            return redirect('login')


class DeleteRecord(View):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            record = Record.objects.get(id=request.GET['id'])
            balance = record.id_balance
            balance.ajust(not(bool(record.record_type)), record.value)
            record.delete()
            return redirect('app')
        else:
            return redirect('login')


class DuplicateRecord(View):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            record = Record.objects.get(id=request.GET['id'])
            balance = Balance.objects.get(id=record.id_balance.id)
            rec = Record(name=record.name, value=record.value, id_balance=record.id_balance,
                         id_tag=record.id_tag, record_type=record.record_type)
            rec.save()
            balance.ajust(rec.record_type, rec.value)
            return redirect('app')
        else:
            return redirect('login')
