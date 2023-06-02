from django.shortcuts import render
from customer.models import *
from customer.serializers import *

# Create youe views here.
from rest_framework.views import status
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.permissions import AllowAny,IsAuthenticated

class Getcustomerview(APIView):

    def get(self,request):
        instance = Customers.objects.all()
        serializers = GetCustomerSerializers(instance,many=True)
        return Response(serializers.data)

    def post(self,request):
      params=request.data
      print("data",params)
      ser=GetCustomerSerializers(data=params)
      ser.is_valid(raise_exception=True)
      ser.save()
      return Response({"message":"Save sucessfully"})


class GetAddressview(APIView):

    def get(self,request):
        instance = CustomerAddress.objects.all()
        serializers = GetAddressSerializers(instance,many=True)
        return Response(serializers.data)
    
class CustomerDetailAddressView(APIView):

    def get(self,request,pk):
        instance = Customers.objects.filter(id=pk)
        serializers = GetCustomerAddressSerializer(instance,many=True)
        return Response(serializers.data)
        