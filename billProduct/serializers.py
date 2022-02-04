from rest_framework import serializers
from billProduct.models import BillProduct

class BillProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillProduct
        fields = ['bill_id', 'product_id']
