from django.db import models

class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    account = models.IntegerField()
    description = models.TextField()
    name = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
