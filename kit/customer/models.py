from django.db import models


# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    country = models.CharField(max_length=40, default='China')

    def __str__(self):
        return self.name
