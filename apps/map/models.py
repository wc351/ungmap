from django.contrib.gis.db import models


class Pics(models.Model):
    """Pics model."""
    name = models.CharField(max_length=40)
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Teachers(models.Model):
    """ Teacher model.
    """
    name = models.CharField(max_length=150)
    pic = models.ForeignKey(Pics)
    subject = models.CharField(max_length=40)
    building = models.CharField(max_length=40)
    building_num = models.IntegerField(max_length=5)
    office_num = models.IntegerField(max_length=5)
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Teachers'

    def __str__(self):
        return self.name


class Recreation(models.Model):
    """ Recreation model.
    """
    name = models.CharField(max_length=50)
    pic = models.ForeignKey(Pics)
    geom = models.MultiPolygonField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Rec Areas'

    def __str__(self):
        return self.name


class Classrooms(models.Model):
    """ Classrooms model.
    """
    name = models.CharField(max_length=15)
    class_num = models.FloatField(max_length=10)
    pics = models.ForeignKey(Pics)
    building = models.CharField(max_length=40)
    building_num = models.IntegerField(max_length=5)
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Classrooms'

    def __str__(self):
        return self.name


class ParkingLots(models.Model):
    """ Parking lot models.
    """
    lot_name = models.CharField(max_length=5)
    description = models.CharField(max_length=150)
    pics = models.ForeignKey(Pics)
    geom = models.MultiPolygonField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Parking_Lots'

    def __str__(self):
        return self.lot_name


class Administration(models.Model):
    """ Teacher model.
    """
    name = models.CharField(max_length=150)
    pic = models.ForeignKey(Pics)
    subject = models.CharField(max_length=40)
    building = models.CharField(max_length=40)
    building_num = models.IntegerField(max_length=5)
    office_num = models.IntegerField(max_length=5)
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Administration'

    def __str__(self):
        return self.name
