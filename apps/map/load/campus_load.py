import shapefile
from apps.map.models import Campus
import django
django.setup()


path1='C:/Users/wecox1088/Desktop/UNGMap_Data/Campus/campuses.shp'

sf = shapefile.Reader(path1)
sr = sf.shapeRecords()


for r in sr:
    geom = r.shape.__geo_interface__

    d = Campus(name=r.record[0], location=r.record[1], geom="POINT({} {})".format(r.shape.points[0][0], r.shape.points[0][1]))
    d.save()
print "Done"