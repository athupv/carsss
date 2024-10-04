from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    selling_quantity = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    manufacturing_year = models.IntegerField()

    def __str__(self):
        return self.name
