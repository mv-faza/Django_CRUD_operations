from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

class employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=CASCADE)

