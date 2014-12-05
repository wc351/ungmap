import shapefile
import json
from apps.map.models import Campus, Building
import django
django.setup()


path1 = 'C:/Users/clsmit8703/Desktop/Data/Gainesville_buildings.shp'
path2 = 'C:/Users/clsmit8703/Desktop/Data/Oconee_buildings.shp'
path3 = 'C:/Users/clsmit8703/Desktop/Data/Cumming_buildings.shp'
path4 = 'C:/Users/clsmit8703/Desktop/Data/Dahlonega_buildings2.shp'

sf1 = shapefile.Reader(path1)
sr1 = sf1.shapeRecords()
sf2 = shapefile.Reader(path2)
sr2 = sf2.shapeRecords()
sf3 = shapefile.Reader(path3)
sr3 = sf3.shapeRecords()
sf4 = shapefile.Reader(path4)
sr4 = sf4.shapeRecords()

Gainesville_cam = Campus.objects.filter(pk=1).first()
Oconee_cam = Campus.objects.filter(pk=4).first()
Dahlonega_cam = Campus.objects.filter(pk=3).first()
Cumming_cam = Campus.objects.filter(pk=2).first()

for r in sr1:
    geom = r.shape.__geo_interface__

    d = Building(name=r.record[2], desc=r.record[3], build_num=r.record[4], alter_name=r.record[5], campus=Gainesville_cam, geom=json.dumps(geom))
    d.save()
print "Gainesville Done"

for r in sr2:
    geom = r.shape.__geo_interface__

    d = Building(name=r.record[1], desc=r.record[10], build_num=r.record[9], alter_name=r.record[11], campus=Oconee_cam, geom=json.dumps(geom))
    d.save()
print "Oconee Done"

for r in sr3:
    geom = r.shape.__geo_interface__

    d = Building(name=r.record[12], desc=r.record[13], build_num=r.record[1], alter_name=r.record[15], campus=Cumming_cam, geom=json.dumps(geom))
    d.save()
print "Cumming Done"

for r in sr4:
    geom = r.shape.__geo_interface__

    d = Building(name=r.record[12], desc=r.record[13], build_num=r.record[1], alter_name=r.record[15], campus=Dahlonega_cam, geom=json.dumps(geom))
    d.save()
print "Dahlonega Done"