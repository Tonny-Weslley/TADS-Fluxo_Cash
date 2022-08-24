from django.contrib import admin

from .models import Balance, Record, Tag

# Register your models here.

admin.site.register(Record)
admin.site.register(Tag)
admin.site.register(Balance)
