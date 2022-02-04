from django.db import models

class Client(models.Model):
    document = models.CharField(max_length=11)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
