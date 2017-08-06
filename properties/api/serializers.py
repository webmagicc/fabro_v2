from rest_framework import serializers
from properties.models import CategoryProperty, ProductProperty


class CategoryPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProperty
        fields = '__all__'

class ProductPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProperty
        fields = '__all__'



