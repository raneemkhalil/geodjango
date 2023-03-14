from django.contrib.gis.db import models
from django.db import models as md


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    nname = md.CharField(max_length=50, default='')
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()


    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.MultiPolygonField(srid=4326, null=True, blank=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class WorldBorderJson(models.Model):

    objectid = models.IntegerField(default=5)
    diameter = models.FloatField(default=.5)
    label = models.CharField(max_length=80, default='')
    l_scaled = models.IntegerField(default=5)
    v = models.FloatField(default=.5)
    shape_leng = models.FloatField(default=.5)
    geom = models.MultiLineStringField(srid=4326)

    # Returns the string representation of the model.
    def __str__(self):
        return self.label


class LeakHotspot(models.Model):

    elevation = models.FloatField(default=.5)
    emitter_k = models.FloatField(default=.5)
    label = models.CharField(max_length=80, default='')
    p = models.FloatField(default=.5)
    runid = models.CharField(max_length=80, default='')
    leak = models.FloatField(default=.5)
    color = models.CharField(max_length=80, default='')
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return self.label


class Ran(md.Model):
    elevation = models.FloatField(default=.5)
    emitter_k = md.FloatField(default=.5)


class Point(models.Model):
    coords = models.PointField()
    