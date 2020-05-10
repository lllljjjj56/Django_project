from django.db import models
from customer.models import Customer
from django.utils import timezone


# Create your models here.
class Commodity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    custom = models.ForeignKey(Customer, on_delete=models.CASCADE)
    commodity = models.ManyToManyField(Commodity)
    price = models.IntegerField(default=100)
    date = models.DateTimeField(default=timezone.now)
    remarks = models.CharField(max_length=1000, default='comment here')

    def __str__(self):
        return str(self.id)
