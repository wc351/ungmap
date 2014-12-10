import shapefile
import json
from apps.map.models import Campus, ParkingLots
import django
django.setup()


path1='C:/Users/clsmit8703/Desktop/Data/Gainesville_Parkinglots_disolv.shp'
path2='C:/Users/clsmit8703/Desktop/Data/Cumming_parkinglots'



sf1 = shapefile.Reader(path1)
sr1 = sf1.shapeRecords()

Gainesville_cam = Campus.objects.filter(pk=1).first()
Oconee_cam = Campus.objects.filter(pk=4).first()


for r in sr1:
    geom = r.shape.__geo_interface__

    d = ParkingLots(lot_name=r.record[0], campus=Gainesville_cam, desc=r.record[1], geom=json.dumps(geom))
    d.save()
print "Done"

sf2 = shapefile.Reader(path2)
sr2 = sf2.shapeRecords()

for r in sr2:
    geom = r.shape.__geo_interface__

    d = ParkingLots(lot_name=r.record[2], campus=Oconee_cam, desc=r.record[5], geom=json.dumps(geom))
    d.save()
print "Done"