from django.contrib import admin

# Register your models here.
from apps.map import models

admin.site.register(models.Campus)
admin.site.register(models.Building)
admin.site.register(models.Classrooms)
admin.site.register(models.Faculty)
admin.site.register(models.Recreation)
admin.site.register(models.ParkingLots)
admin.site.register(models.CampusPics)
admin.site.register(models.BuildingPics)
admin.site.register(models.ParkingLotPics)