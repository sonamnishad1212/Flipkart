from rest_framework import serializers
from customer.models import *

#create your views here.

class  GetCustomerSerializers(serializers.ModelSerializer):
    
    class Meta:
        model =Customers
        fields ="__all__"

class  GetCustomerAddressSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerAddress
        fields = "__all__"


class CustomersDetailsAddressSerializer(serializers.ModelSerializer):
    customer_address = GetCustomerAddressSerializers(many=True)

    class Meta:
        model = CustomerAddress
        fields = ('first_name','last_name ','  moblie ',' address',' age',' country','dob','city')

