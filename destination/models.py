from django.db import models

# Create your models here.
class Destination(models.Model):
    id              = models.AutoField(primary_key=True)
    city            = models.CharField(max_length=120)
    averagePrice    = models.DecimalField(decimal_places=2, max_digits=10000)
    propertyCount   = models.IntegerField()
    imageUrl        = models.TextField(blank=True, null=True) 
    imageAlt        = models.CharField(max_length=120, null=True)
    