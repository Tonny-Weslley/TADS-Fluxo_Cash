from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#000000')


class Record(models.Model):
    name = models.CharField(max_length=100)
    id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    id_tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Record_type = models.BooleanField()
    date_in = models.DateField()
