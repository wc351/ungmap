from django.contrib.gis.db import models
from django.core.urlresolvers import reverse_lazy


class Campus(models.Model):
    """ Campus model."""
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    geom = models.PointField()
    box = models.PolygonField(default=None, null=True, blank=True)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campuses'

    def get_absolute_url(self):
        return reverse_lazy('map:campus_dview', kwargs={'pk': self.pk})

    def __str__(self):
        return "{}-{}".format(self.pk, self.name)


class Building(models.Model):
    """Building model"""

    name = models.CharField(max_length=75)
    alter_name = models.CharField(max_length=500, null=True)
    desc = models.CharField(max_length=100, null=True)
    build_num = models.CharField(max_length=10, null=True)
    campus = models.ForeignKey(Campus)
    geom = models.GeometryField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Building'

    def get_absolute_url(self):
        return reverse_lazy('map:building_dview', kwargs={'pk': self.pk})

    def __str__(self):
        return "Building Name: {0}, {1} Campus".format(self.name, self.campus.name)


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

    def get_absolute_url(self):
        return reverse_lazy('map:office_dview', kwargs={'pk': self.pk})

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
        verbose_name_plural = 'Faculty'

    def get_absolute_url(self):
        return reverse_lazy('map:faculty_dview', kwargs={'pk': self.pk})

    def __str__(self):
        return "Name: {0}, {1} Campus".format(self.name, self.campus.name)


class Recreation(models.Model):
    """ Recreation model.
    """
    name = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
    geom = models.GeometryField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Rec Areas'

    def get_absolute_url(self):
        return reverse_lazy('map:recreation_dview', kwargs={'pk': self.pk})

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

    def get_absolute_url(self):
        return reverse_lazy('map:classroom_dview', kwargs={'pk': self.pk})

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

    def get_absolute_url(self):
        return reverse_lazy('map:parkinglot_dview', kwargs={'pk': self.pk})

    def __str__(self):
        return "{0}, {1} Campus".format(self.lot_name, self.campus.name)


class ParkingSpots(models.Model):
    """Parking spot model
    """
    spot_type = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
    geom = models.GeometryField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Parking Spots'

    def __str__(self):
        return "{0}, {1} Campus".format(self.spot_type, self.campus.name)


class ParkingLotLines(models.Model):
    """Parking lot line model
    """
    name = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
    geom = models.LineStringField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Parking Lot Lines'

    def __str__(self):
        return "{0}, {1} Campus".format(self.name, self.campus.name)


class CallBoxes(models.Model):
    """Call Box Model"""
    name = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
    geom = models.PointField()
    objects = models.GeoManager()


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
    building = models.ForeignKey(Building)
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