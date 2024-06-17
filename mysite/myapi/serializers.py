from rest_framework import  serializers

from .models  import Customer, Order


import  africastalking

from .tests  import username,api_key


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Customer
        fields = ('id', 'name', 'code','phone_number')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id','item', 'amount','time')


        def create(self,validated_data):
            order = Order.objects.create(**validated_data)



#Function for sending sms via africasTalking
def sendsms():
     #initialising SDK
    africastalking.initialize(username, api_key) 


    sms = africastalking.SMS 
    #using service Synchrously

    response = sms.send("Dear customer,new orders are available kindly check them out")
    

