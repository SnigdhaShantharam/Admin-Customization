from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [

    path('',views.AllData.as_view(), name="all"),
    path('sellers/',views.SellersView.as_view(), name="sellers"),
    path('products/',views.ProductsView.as_view(), name="products"),
    path('customers/',views.CustomersView.as_view(), name="customers"),
    path('seller/search/',views.SellerSearch.as_view(), name="customers"),
]