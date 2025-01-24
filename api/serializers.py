from api.models import *
from rest_framework import serializers

class ProviderInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderInvoice
        fields = '__all__'