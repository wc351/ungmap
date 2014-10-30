import shapefile
import json
from apps.map.models import Campus, Building
import django
django.setup()


path1='C:/Users/crlyli0476/Desktop/ungmap_reproject/Gainesville_buildings.shp'
path2='C:/Users/crlyli0476/Desktop/ungmap_reproject/Oconee_buildings.shp'

sf1 = shapefile.Reader(path1)
sr1 = sf1.shapeRecords()

sf2 = shapefile.Reader(path2)
sr2 = sf2.shapeRecords()

Gainesville_cam = Campus.objects.filter(pk=1)
Oconee_cam = Campus.objects.filter(pk=2)


for r in sr1:
    geom = r.shape.__geo_interface__
    d = Building(name=r.record[4], desc=r.record[5], build_num=r.record[6], campus=Gainesville_cam, geom=json.dumps(geom))
    print d
    d.save()

for r in sr2:
    geom = r.shape.__geo_interface__
    d = Building(name=r.record[1], desc = r.record[10], build_num=r.record[9], campus=Oconee_cam, geom=json.dumps(geom))
    print d
    d.save()

#sf3 = shapefile.Reader(path3)
#sr3 = sf1.shapeRecords()
#sf4 = shapefile.Reader(path4)
#sr4 = sf1.shapeRecords()

#Dahlonega_cam = Campus.objects.filter(pk=3)
#Cumming_cam = Campus.objects.filter(pk=4)

#for r in sr3:
#    geom = r.shape.__geo_interface__
#    d = Building(name=r.record[], desc = r.record[], build_num=r.record[], campus=Dahlonega_cam, geom=json.dumps(geom))
#    print d
#    d.save()

#for r in sr4:
#    geom = r.shape.__geo_interface__
#    d = Building(name=r.record[], desc = r.record[], build_num=r.record[], campus=Cumming_cam, geom=json.dumps(geom))
#    print d
#    d.save()