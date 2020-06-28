from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Departement(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    pref = models.CharField(max_length=200)
    sous_pref_one = models.CharField(max_length=200)
    sous_pref_two = models.CharField(max_length=200)
    sous_pref_three = models.CharField(max_length=200, null=True)
    sous_pref_four = models.CharField(max_length=200, null=True)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)


class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
