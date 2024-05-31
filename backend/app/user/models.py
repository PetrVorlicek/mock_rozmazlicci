from django.db import models
from django.contrib.auth.models import User
from app.models import IDModel
from eshop.models import Item

# Create your models here.
class Order(IDModel):
    
    STATE_CHOICE = {
        "CR":"CREATED",
        "CA":"CANCELED",
        "CO":"BEING COMPLETED",
        "SH":"SHIPPED",
        "DE":"DELIVERED",}
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICE,default="CR")

    def get_total(self) -> float:
        item_sets: list[OrderItem] = self.orderitem_set.all()
        total = 0
        for item_set in item_sets:
            total = item_set.item.price * item_set.quantity
        # decimal -> float conversion
        return float(total)    
    
class OrderItem(IDModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)