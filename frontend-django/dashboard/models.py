from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    dcu_id = models.CharField(max_length=512)
    modules = models.CharField(max_length=512)
