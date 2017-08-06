from .serializers import (
	CategorySerializer,
	BrandSerializer,
	ImagesSerializer,
	OfferSerializer,
	ProductListSerializer,
	ProductSerializer,)

from rest_framework import viewsets

from shop.models import Category, Brand, Product, Images, Offer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
	model = Category
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
	model = Brand
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
	model = Product
	queryset = Product.objects.all()
	serializer_class = ProductListSerializer
	def retrieve(self,pk=None):
		pass
