from django.db import models
from app.models import IDModel

# Create your models here.
class Item(IDModel):
    description = models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image_path = models.CharField(max_length=128, blank=True)
    stock = models.IntegerField(default=0)
    visible = models.BooleanField(default=False)
