from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tool(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.description


class Lease(models.Model):
    lessee = models.ForeignKey(User, on_delete=models.CASCADE)
    thing = models.ForeignKey(Tool, on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True)
    stop = models.DateTimeField(null = True)