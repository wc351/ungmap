from django.db import models


class Pics(models.Model):
    """Pics model."""
    name = models.CharField(max_length=40)
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


