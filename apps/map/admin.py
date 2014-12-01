from django.contrib.gis import admin

# Register your models here.
from apps.map import models

admin.site.register(models.Campus, admin.GeoModelAdmin)
admin.site.register(models.Building, admin.GeoModelAdmin)
admin.site.register(models.Classrooms)
admin.site.register(models.Faculty, admin.GeoModelAdmin)
admin.site.register(models.Recreation)
admin.site.register(models.ParkingLots, admin.GeoModelAdmin)
admin.site.register(models.ParkingSpots, admin.GeoModelAdmin)
admin.site.register(models.ParkingLotLines, admin.GeoModelAdmin)
admin.site.register(models.CallBoxes, admin.GeoModelAdmin)
admin.site.register(models.CampusPics)
admin.site.register(models.BuildingPics)
admin.site.register(models.ParkingLotPics)