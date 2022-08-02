from django.urls import include, path

from .views.public_views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
