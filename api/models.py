from django.db import models
from django.conf import settings

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=30)
    read_as = models.BooleanField(default=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    class Meta:
        unique_together = ['name', 'owner']
