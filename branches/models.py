from django.db import models
from django.contrib.gis.db import models
from djgeojson.fields import PointField

# Create your models here.
class Main_Office(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField(srid= 4326)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Issues_Addressed(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Regional_Office(models.Model):
    regional_branch = models.ForeignKey(Main_Office,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    location = models.PointField(srid= 4326)
    number_of_staff = models.IntegerField()
    issues_addressed = models.ManyToManyField(Issues_Addressed, blank=True)
    slug = models.SlugField(null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Field_Offices(models.Model):
    field_branch = models.ForeignKey(Regional_Office, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number_of_staff = models.IntegerField()
    issues_addressed = models.ManyToManyField(Issues_Addressed, blank=True)
    name = models.CharField(max_length=50)
    location = models.PointField(srid= 4326)
    slug = models.SlugField(null=True, blank=True)
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Counties(models.Model):
    objectid = models.BigIntegerField(null=True)
    id_field = models.BigIntegerField(null=True)
    county_nam = models.CharField(max_length=80,null=True )
    const_code = models.BigIntegerField(null=True)
    constituen = models.CharField(max_length=80, null=True)
    county_cod = models.BigIntegerField(null=True)
    shape_leng = models.FloatField(null=True)
    shape_area = models.FloatField(null=True)
    geom = models.MultiPolygonField(srid=4326)


    def __unicode__(self):
    	return self.counties