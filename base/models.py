from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=50)
    sign = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=10, decimal_places=5)


    def __str__(self):
        return self.name


class Country(models.Model):
    country_name = models.CharField(max_length=50, unique=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.country_name
    
    