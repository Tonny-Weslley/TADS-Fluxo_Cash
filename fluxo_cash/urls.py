from django.urls import include, path

from .views.private_views import *
from .views.public_views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),

    # Private views
    path('app/', App.as_view(), name='app'),
    path('logout/', Logout.as_view(), name='logout'),
    path('add_record/', AddRecord.as_view(), name='add_record'),
    path('add_balance/', AddBalance.as_view(), name='add_balance'),
    path('delete_balance', DeleteBalance.as_view(), name='delete_balance'),
    path('balance_viewer/', BalanceView.as_view(), name='balance_viewer'),
    path('duplicate_record/', DuplicateRecord.as_view(), name='duplicate_record'),
    path('delete_record/', DeleteRecord.as_view(), name='delete_record'),
]
