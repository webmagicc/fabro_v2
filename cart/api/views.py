from .serializers import (
	CategorySerializer,
	BrandSerializer,
	ImagesSerializer,
	OfferSerializer,
	ProductListSerializer,
	ProductSerializer,)

from rest_framwork import viewsets

from shop.models import Category, Brand, Product, Images, Offer


class CategoryListViewSet(viewsets.ReadOnlyModelViewSet):
	model = Category
	queryset = Category.objects.all()
