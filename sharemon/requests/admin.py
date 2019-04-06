from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Post)
admin.site.register(models.Event)
admin.site.register(models.Student)
admin.site.register(models.LostAndFound)