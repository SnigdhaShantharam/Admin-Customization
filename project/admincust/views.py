from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import filters

from .serializers import ProductSerializer, SellerSerializer, CustomerSerializer
from .models import Customer, Seller, Product
import django_filters.rest_framework
from django.contrib.auth.models import User
# from myapp.serializers import UserSerializer
from rest_framework import generics

class AllData(GenericAPIView):

    def get(self, request):
        customers = Customer.objects.all()
        seller = Seller.objects.all()
        products = Product.objects.all()
        cserializer = CustomerSerializer(customers, many = True)
        pserializer = ProductSerializer(products, many = True)
        sserializer = SellerSerializer(seller, many = True)
        response = {
            'customers': cserializer.data,
            'seller': sserializer.data,
            'products': pserializer.data,
        }
        return Response(response)

class SellersView(GenericAPIView):
    queryset = Seller.objects.all()
    def get(self, request):
        queryset = Seller.objects.all()
        sserializer = SellerSerializer(queryset, many = True)
        response = {
            'seller': sserializer.data,
        }
        return Response(response)

class ProductsView(GenericAPIView):
    queryset = Product.objects.all()
    def get(self, request):
        seller = Product.objects.all()
        sserializer = ProductSerializer(seller, many = True)
        response = {
            'products': sserializer.data,
        }
        return Response(response)

class CustomersView(GenericAPIView):
    queryset = Customer.objects.all()
    
    def get(self, request):
        seller = Customer.objects.all()
        sserializer = CustomerSerializer(seller, many = True)
        response = {
            'customers': sserializer.data,
        }
        return Response(response)

# class SellerSearch(generics.ListAPIView):
    
#     queryset = Seller.objects.all()
#     serializer_class = SellerSerializer
#     filter_backends = [filters.SearchFilter]
#     lookup_url_kwarg = 'search'
#     search_fields = ['seller_name']

class SellerSearch(generics.ListAPIView):
    model = Seller
    serializer_class = SellerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['customers__customers']

    def get_queryset(self):
        # query = self.request.GET.get('searchbar')
        # query = 'mtr'
        # object_list = Seller.objects.filter(
        #     Q(seller_name__icontains=query)
        # )
        search = self.request.query_params.get('search')
        print(search)
        cust = Customer.objects.filter(name=search).first()
        object_list = Seller.objects.filter(
            Q(customers__in=[cust])
        )
        return object_list