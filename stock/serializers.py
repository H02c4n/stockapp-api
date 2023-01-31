from rest_framework import serializers
from .models import Firm, Category, Brand, Product, Purchases, Sales




class FirmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Firm
        fields = ['id','name','phone','address']


class CateorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name']


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields =['id','name']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id' ,'name', 'category', 'brand', 'stock']




class PurchasesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Purchases
        fileds = '__all__'




class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = '__all__'