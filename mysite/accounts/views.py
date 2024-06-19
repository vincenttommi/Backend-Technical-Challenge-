from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status, viewsets
from django.shortcuts import render

from .serializers import CustomerSerializer, OrderSerializer
from .models import Customer, Order


# Create your views here.
class CustomerViewSet(LoginRequiredMixin, viewsets.ModelViewSet):

    queryset = Customer.objects.all().order_by('code')
    serializer_class = CustomerSerializer


class OrderViewSet(LoginRequiredMixin, viewsets.ModelViewSet):

    queryset = Order.objects.all().order_by('time')
    serializer_class = OrderSerializer
