from django.shortcuts import render, HttpResponse
from .models import Firm, Category, Brand, Product, Purchases, Sales
from .serializers import FirmSerializer, CateorySerializer, BrandSerializer, ProductSerializer, PurchasesSerializer, SalesSerializer

from rest_framework.viewsets import ModelViewSet

# Create your views here.



class  FirmMVS(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer