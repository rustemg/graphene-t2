from django.db import models


class Organization(models.Model):
    full_name = models.CharField(max_length=250)
    registration_date = models.DateField()
