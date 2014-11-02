from django.contrib.gis.db import models


class Campus(models.Model):
    """ Campus model."""
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campuses'

    def __str__(self):
        return self.name


class Building(models.Model):
    """Building model"""

    name = models.CharField(max_length=75)
    desc = models.CharField(max_length=100, null=True)
    build_num = models.CharField(max_length=10, null=True)
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
    campus = models.ForeignKey(Campus)
    building = models.ForeignKey(Building)
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=40)
    office_num = models.CharField(max_length=50, null=True)
    phone_num = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=75)

    class Meta:
        verbose_name = 'Faculty'

    def __str__(self):
        return self.name


class Recreation(models.Model):
    """ Recreation model.
    """
    name = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
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
    desc = models.CharField(max_length=150, null=True)
    geom = models.GeometryField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Parking_Lots'
        verbose_name_plural = 'Parking Lots'

    def __str__(self):
        return self.lot_name


class CampusPics(models.Model):
    """Pics model."""

    name = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus)
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class BuildingPics(models.Model):
    """Pics model."""

    name = models.CharField(max_length=100)
    campus = models.ForeignKey(Building)
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class ParkingLotPics(models.Model):
    """Pics model."""

    name = models.CharField(max_length=100)
    campus = models.ForeignKey(ParkingLots)
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name