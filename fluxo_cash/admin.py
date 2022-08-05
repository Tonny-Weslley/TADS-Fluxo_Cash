from django.contrib import admin

from .models import Record, Tag, UserProfile

# Register your models here.

admin.site.register(Record)
admin.site.register(Tag)
admin.site.register(UserProfile)
