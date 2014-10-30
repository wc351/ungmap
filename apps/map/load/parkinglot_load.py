import shapefile
import json
from apps.map.models import Campus, ParkingLots
import django
django.setup()


path1='C:/Users/crlyli0476/Desktop/ungmap_reproject/Gainesville_Parkinglots_disolv.shp'


sf1 = shapefile.Reader(path1)
sr1 = sf1.shapeRecords()

Gainesville_cam = Campus.objects.filter(pk=1)


for r in sr1:
    geom = r.shape.__geo_interface__
    d = ParkingLots(lot_name=r.record[1], campus=Gainesville_cam, desc=r.record[2], geom=json.dumps(geom))
    print d
    d.save()