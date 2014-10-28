from django.contrib.gis.db import models


class Pics(models.Model):
    """Pics model."""

    name = models.CharField(max_length=100)
    pic_campus = models.CharField(max_length=75)
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Campus(models.Model):
    """ Campus model."""
    name = models.CharField(max_length=50)
    pic = models.ForeignKey(Pics)
    location = models.CharField(max_length=50)
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Campus'

    def __str__(self):
        return self.name


class Building(models.Model):
    """Building model"""

    name = models.CharField(max_length=75)
    desc = models.CharField(max_length=100)
    pic = models.ForeignKey(Pics)
    build_num = models.CharField(max_length=10)
    campus = models.ForeignKey(Campus)
    geom = models.GeometryField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Building'

    def __str__(self):
        return self.name


class Office(models.Model):
    """ Office model."""
    name = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
    building = models.ForeignKey(Building)
    num = models.IntegerField(max_length=5)
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
    title = models.CharField(max_length=40)
    campus = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    office_num = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    primary_campus = models.ForeignKey(Campus)
    department = models.CharField(max_length=75)
    geom = models.GeometryField()
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
    geom = models.GeometryField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Rec Areas'

    def __str__(self):
        return self.name


class Classrooms(models.Model):
    """ Classrooms model.
    """
    name = models.CharField(max_length=15)
    campus = models.ForeignKey(Campus)
    num = models.FloatField(max_length=10)
    building = models.ForeignKey(Building)
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Classrooms'

    def __str__(self):
        return self.name


class ParkingLots(models.Model):
    """ Parking lot models.
    """
    lot_name = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
    description = models.CharField(max_length=150)
    pics = models.ForeignKey(Pics)
    geom = models.GeometryField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Parking_Lots'

    def __str__(self):
        return self.lot_name



