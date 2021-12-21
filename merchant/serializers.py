from rest_framework import serializers
from .models import Merchant
# class MerchantSerializer(serializers.Serializer):
#     merchant_name = serializers.CharField()
#     merchant_code = serializers.CharField()
#     merchant_address = serializers.CharField()


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'
        

# password
# confirm_password 
# new_password 
