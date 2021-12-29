from django.db.models import JSONField
from django.db import models


class InputModel(models.Model):
    field = models.CharField(max_length=50)
    data = JSONField()

    def __str__(self):
        return self.data

    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'