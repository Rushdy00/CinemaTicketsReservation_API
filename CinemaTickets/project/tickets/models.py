from django.db import models
from django.contrib.auth.models import User
#Guest -- hall -- reservation

class Movie(models.Model):
    hall = models.CharField(max_length=10,)
    movie = models.CharField(max_length=10)
    date = models.CharField(max_length=10)


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    name = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)

class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservations', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservations', on_delete=models.CASCADE)