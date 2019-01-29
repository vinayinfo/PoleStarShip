from django.db import models


class ShipName(models.Model):
    """Ship Name model"""
    imo = models.CharField(max_length=30)


class ShipLocation(models.Model):
    """Ship location details"""
    imo = models.ForeignKey(ShipName, on_delete=models.deletion.CASCADE,)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    ship_date = models.DateTimeField()
