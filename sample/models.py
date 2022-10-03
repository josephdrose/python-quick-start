from django.db import models

class Order(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()
    sku = models.CharField(max_length=100)