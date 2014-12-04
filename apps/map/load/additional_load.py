import shapefile
import json
import glob
from apps.map.models import Campus, Recreation, ParkingSpots, ParkingLotLines, CallBoxes
import django
django.setup()

Gainesville_cam = Campus.objects.filter(pk=1).first()


path1='C:/Users/clsmit8703/Desktop/Data/ungmap_reproject/tennis.shp'
sf1 = shapefile.Reader(path1)
sr1 = sf1.shapeRecords()

for r in sr1:
    geom = r.shape.__geo_interface__
    d = Recreation(name=r.record[1], campus=Gainesville_cam, geom=json.dumps(geom))
    d.save()
print "Done"

path2='C:/Users/clsmit8703/Desktop/Data/ungmap_reproject/track.shp'
sf2 = shapefile.Reader(path2)
sr2 = sf2.shapeRecords()

for r in sr2:
    geom = r.shape.__geo_interface__
    d = Recreation(name=r.record[7], campus=Gainesville_cam, geom=json.dumps(geom))
    d.save()
print "Done"


path3='C:/Users/clsmit8703/Desktop/Data/ungmap_reproject/parkinglines.shp'
sf3 = shapefile.Reader(path3)
sr3 = sf3.shapeRecords()

for r in sr3:
    geom = r.shape.__geo_interface__
    d = ParkingLotLines(name='parking', campus=Gainesville_cam, geom=json.dumps(geom))
    d.save()
print "Done"

path4='C:/Users/crlyli0476/Desktop/ungmap/ungmap_reproject/callboxes.shp'
sf4 = shapefile.Reader(path4)
sr4 = sf4.shapeRecords()
for r in sr4:
    d = CallBoxes(name=r.record[1], campus=Gainesville_cam, geom="POINT({} {})".format(r.shape.points[0][0],
                                                                                      r.shape.points[0][1]))

    d.save()
print "Done"

dir_path = 'C:/Users/clsmit8703/Desktop/Data/ungmap_reproject/parkingSpot_files'
files = glob.glob(dir_path + '/*.shp')

for file in files:
    sf = shapefile.Reader(file)
    sr = sf.shapeRecords()
    for r in sr:
        geom = r.shape.__geo_interface__

        d = ParkingSpots(spot_type=r.record[1], campus=Gainesville_cam, geom=json.dumps(geom))
        d.save()
print "Done"