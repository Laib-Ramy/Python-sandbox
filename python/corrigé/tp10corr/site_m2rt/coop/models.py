from django.db import models
from django.contrib.auth.models import User

class Tool(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.description
