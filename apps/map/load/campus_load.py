import shapefile
from apps.map.models import Campus
import django
django.setup()


path1='C:/Users/crlyli0476/Desktop/ungmap_reproject/Campus/campuses.shp'

sf = shapefile.Reader(path1)
sr = sf.shapeRecords()


for r in sr:
    geom = r.shape.__geo_interface__

    d = Campus(name=r.record[0], location=r.record[1], geom="POINT({} {})".format(r.shape.points[0][0], r.shape.points[0][1]))
    print d
    d.save()