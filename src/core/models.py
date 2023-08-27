from django.contrib.auth.models import User as AuthUser
from django.db import models


class Currency(models.Model):
    code3 = models.CharField(max_length=3)


class Cource(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    course = models.DecimalField(max_digits=16, decimal_places=4)
    update_time = models.DateTimeField()


class User(models.Model):
    auth_user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)


class Card(models.Model):
    currcency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=16, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Transaction(models.Model):
    sender_card = models.ForeignKey(Card, related_name="sender_card_id", on_delete=models.CASCADE)
    receiver_card = models.ForeignKey(Card, related_name="receiver_card_id", on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=16, decimal_places=2)
    time = models.DateTimeField()


class SystemTransaction(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=16, decimal_places=2)
    note = models.CharField(max_length=100)
    time = models.DateTimeField()
