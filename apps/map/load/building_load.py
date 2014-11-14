import shapefile
import json
from apps.map.models import Campus, Building
import django
django.setup()


path1 = 'C:/Users/wecox1088/Desktop/ungmap_data/Gainesville_buildings.shp'
path2 = 'C:/Users/wecox1088/Desktop/ungmap_data/Oconee_buildings.shp'
path3 = 'C:/Users/wecox1088/Desktop/ungmap_data/Cumming_buildings.shp'
path4 = 'C:/Users/wecox1088/Desktop/ungmap_data/Dahlonega_buildings2.shp'

sf1 = shapefile.Reader(path1)
sr1 = sf1.shapeRecords()
sf2 = shapefile.Reader(path2)
sr2 = sf2.shapeRecords()
sf3 = shapefile.Reader(path3)
sr3 = sf3.shapeRecords()
sf4 = shapefile.Reader(path4)
sr4 = sf4.shapeRecords()

Gainesville_cam = Campus.objects.filter(pk=1).first()
Oconee_cam = Campus.objects.filter(pk=2).first()
Dahlonega_cam = Campus.objects.filter(pk=3).first()
Cumming_cam = Campus.objects.filter(pk=4).first()

for r in sr1:
    geom = r.shape.__geo_interface__

    d = Building(name=r.record[2], desc=r.record[3], build_num=r.record[4], campus=Gainesville_cam, geom=json.dumps(geom))
    print d
    d.save()

for r in sr2:
    geom = r.shape.__geo_interface__

    d = Building(name=r.record[1], desc=r.record[10], build_num=r.record[9], campus=Oconee_cam, geom=json.dumps(geom))
    print d
    d.save()

for r in sr3:
    geom = r.shape.__geo_interface__

    d = Building(name=r.record[12], desc=r.record[13], build_num=r.record[1], campus=Cumming_cam, geom=json.dumps(geom))
    print d
    d.save()

for r in sr4:
    geom = r.shape.__geo_interface__

    d = Building(name=r.record[12], desc=r.record[13], build_num=r.record[1], campus=Dahlonega_cam, geom=json.dumps(geom))
    print d
    d.save()