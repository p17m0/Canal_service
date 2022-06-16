from django.db import models


class Orders(models.Model):
    zakaz = models.TextField(null=False)
    price_d = models.FloatField()
    price_r = models.FloatField()
    date = models.DateField()
