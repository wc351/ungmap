import shapefile
import json
from apps.map.models import Campus
import django
django.setup()


path1='C:/Users/crlyli0476/Desktop/ungmap_reproject/Gainesville_buildings.shp'

sf = shapefile.Reader(path1)
sr = sf.shapeRecords()


for r in sr:
    geom = r.shape.__geo_interface__

    d = Campus(name=r.record[1], location=r.record[2], geom="POINT({} {})".format(r.shape.points[0][0], r.shape.points[0][1]))
    print d
    d.save()