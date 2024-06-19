from  rest_framework  import serializers
from .models import Customer,Order

import africastalking

from  .tests import username,api_key


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Customer
        fields = ('id', 'name','code','phone_number')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order 
        fields = ('id','item','amount', 'time' )

    def create(self, validate_data):
        order = Order.objects.create(**validate_data)


#sending sms via africaTalking
def sendsms():

    #Initializing SDK
    sms = africastalking.SMS

    #using service Sychronously
    response  =  sms.send("Dear Estemeed customer, new orders are available, kindly check them out", ["+254759209325"])
    print(response)