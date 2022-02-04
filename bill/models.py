from django.db import models
from client.models import Client

class Bill(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    nit = models.IntegerField(default=0)
    code = models.IntegerField(default=0)
