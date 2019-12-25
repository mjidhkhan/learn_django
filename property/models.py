from django.db import models

# Create your models here.
class Property(models.Model):
    id              = models.AutoField(primary_key=True)
    title           = models.CharField(max_length=120)
    beds            = models.IntegerField()
    baths           = models.IntegerField()
    priceInCents    = models.IntegerField()
    formattedPrice  = models.DecimalField(decimal_places=2, max_digits=100000)
    reviewCount     = models.IntegerField()
    rating          = models.IntegerField()
    imageUrl        = models.TextField(blank=True, null=True) 
    imageAlt        = models.CharField(max_length=120, null=True)