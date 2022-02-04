from rest_framework import serializers
from client.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['document', 'first_name', 'last_name', 'email']
