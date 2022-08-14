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
]
