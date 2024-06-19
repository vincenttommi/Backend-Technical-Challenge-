from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from  rest_framework import status,viewsets


from .serializers import CustomerSerializer,OrderSerializer
from .models import Customer,Order



class CustomerViewSet(LoginRequiredMixin, viewsets.ModelviewSet)
    queryset  = Customer.objects.all().order_by('code')
    serializer_class  = CustomerSerializer


class OrderViewSet(LoginRequiredMixin,viewsets.ModelViewSet)    

    
# Create your views here.
