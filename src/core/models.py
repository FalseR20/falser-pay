from django.db import models


class Currency(models.Model):
    code3 = models.CharField(max_length=3)


class Cource(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    course = models.DecimalField(max_digits=16, decimal_places=4)
    update_time = models.DateTimeField()
