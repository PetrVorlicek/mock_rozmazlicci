from django.db import models

class IDModel(models.Model):
    id = models.AutoField(primary_key=True, default=None)

    class Meta:
        abstract = True