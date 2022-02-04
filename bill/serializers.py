from rest_framework import serializers
from bill.models import Bill

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['client_id', 'company_name', 'nit', 'code']
