from rest_framework import serializers
from shop.models import Category, Brand, Product, Images, Offer
from properties.models import CategoryProperty, ProductProperty


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)
    offers = OfferSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
