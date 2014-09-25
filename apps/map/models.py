from django.contrib.gis.db import models


class Pics(models.Model):
    """Pics model."""
    name = models.CharField(max_length=40)
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Campus(models.Model):
    """ Campus model."""
    name = models.CharField(max_length=50)
    pic = models.ForeignKey(Pics)
    location = models.CharField(max_length=50)
    geom = models.PolygonField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Campus'

    def __str__(self):
        return self.name


class Building(models.Model):
    """Building model"""
    build_name = models.CharField(max_length=50)
    pic = models.ForeignKey(Pics)
    building_num = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
    geom = models.PolygonField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Building'

    def __str__(self):
        return self.build_name


class Office(models.Model):
    """ Office model."""
    name = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
    office_buil = models.ManyToManyField(Building)
    office_num = models.IntegerField(max_length=5)
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Office'

    def __str__(self):
        return self.name, self.office_buil


class Faculty(models.Model):
    """ Teacher model.
    """
    name = models.CharField(max_length=150)
    campus = models.ForeignKey(Campus)
    pic = models.ForeignKey(Pics)
    title = models.CharField(max_length=40)
    office_buil = models.ForeignKey(Office)
    primary_campus = models.ForeignKey(Campus)
    department = models.CharField(max_length=50)
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Faculty'

    def __str__(self):
        return self.name


class Recreation(models.Model):
    """ Recreation model.
    """
    name = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
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
    class_name = models.CharField(max_length=15)
    campus = models.ForeignKey(Campus)
    class_num = models.FloatField(max_length=10)
    pics = models.ForeignKey(Pics)
    building = models.ForeignKey(Building)
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Classrooms'

    def __str__(self):
        return self.class_name


class ParkingLots(models.Model):
    """ Parking lot models.
    """
    lot_name = models.CharField(max_length=5)
    campus = models.ForeignKey(Campus)
    description = models.CharField(max_length=150)
    pics = models.ForeignKey(Pics)
    geom = models.MultiPolygonField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Parking_Lots'

    def __str__(self):
        return self.lot_name
