import shapefile
import json
from apps.map.models import Campus, ParkingLots
import django
django.setup()


path1='C:/Users/crlyli0476/Desktop/ungmap/ungmap_reproject/Gainesville_Parkinglots_disolv.shp'


sf1 = shapefile.Reader(path1)
sr1 = sf1.shapeRecords()

Gainesville_cam = Campus.objects.filter(pk=1).first()


for r in sr1:
    geom = r.shape.__geo_interface__

    d = ParkingLots(lot_name=r.record[0], campus=Gainesville_cam, desc=r.record[1], geom=json.dumps(geom))
    d.save()
print "Done"