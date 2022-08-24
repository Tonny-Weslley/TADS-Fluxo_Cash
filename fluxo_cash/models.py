from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#000000')

    def __str__(self):
        return self.name


class Balance(models.Model):
    name = models.CharField(max_length=50)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_in = models.DateField(auto_now_add=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def ajust(self, type, rec_value):
        if(type == 1):
            self.value += rec_value
        else:
            self.value -= rec_value
        self.save()

    def __str__(self):
        return (f'{self.id} - {self.id_userProfile.user.username} - {self.value}')


class Record(models.Model):
    name = models.CharField(max_length=100)
    id_balance = models.ForeignKey(
        Balance, on_delete=models.CASCADE)
    id_tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    record_type = models.BooleanField()
    date_in = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return (f'{self.id} - {self.id_userProfile.user.username} - {self.name}')
