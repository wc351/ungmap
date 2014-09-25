from django.contrib import admin

# Register your models here.
from apps.map import models

admin.site.register(models.Pics)
admin.site.register(models.Campus)
admin.site.register(models.Classrooms)
admin.site.register(models.Faculty)
admin.site.register(models.Recreation)
admin.site.register(models.ParkingLots)