from django.db import models
from bill.models import Bill
from product.models import Product

class BillProduct(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
